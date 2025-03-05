import os
import sys
import requests
import hashlib
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_resource(url, output_dir):
    try:
        # Skip data URLs
        if url.startswith('data:'):
            return url

        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Extract filename from URL
            parsed_url = urlparse(url)
            path = parsed_url.path
            filename = os.path.basename(path)
            
            # Handle URLs without filenames
            if not filename.strip():
                url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
                filename = f"resource_{url_hash}"
                if parsed_url.path.endswith('/'):
                    filename += '.html'
            
            # Create output directory if it doesn't exist
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
            
            local_path = os.path.join(output_dir, filename)
            
            # Handle duplicate filenames
            counter = 1
            base_name, ext = os.path.splitext(filename)
            while os.path.exists(local_path):
                filename = f"{base_name}_{counter}{ext}"
                local_path = os.path.join(output_dir, filename)
                counter += 1
            
            with open(local_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return filename
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
    return url

def scrape_and_save(url, selector, output_file):
    # Create output directory
    output_dir = os.path.dirname(output_file)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    # Fetch webpage
    response = requests.get(url)
    response.raise_for_status()
    
    # Parse HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    selected_element = soup.select_one(selector)
    
    if not selected_element:
        raise ValueError(f"No element found with selector: {selector}")
    
    # Find and download linked resources
    elements_with_links = selected_element.find_all(['img', 'script', 'link', 'a'])
    for elem in elements_with_links:
        attr = 'src' if elem.name in ['img', 'script'] else 'href'
        if elem.has_attr(attr):
            absolute_url = urljoin(url, elem[attr])
            if elem.name == 'img' and elem['src'].startswith('data:') and elem.has_attr('data-mathml'):
                # Replace img tag with math tag
                mathml_content = elem['data-mathml']
                math_tag = BeautifulSoup(mathml_content, 'html.parser')
                elem.replace_with(math_tag)
            else:
                local_filename = download_resource(absolute_url, output_dir)
                if local_filename != absolute_url:
                    elem[attr] = local_filename
    
    # Save modified HTML
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(str(selected_element))
    
    print(f"Successfully saved content to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python scrape_content.py <url> <css_selector> <output_file>")
        sys.exit(1)
    
    scrape_and_save(sys.argv[1], sys.argv[2], sys.argv[3])