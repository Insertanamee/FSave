import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_resource(url, base_path, asset_folder):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        parsed_url = urlparse(url)
        path = parsed_url.path.lstrip('/')
        local_path = os.path.join(base_path, asset_folder, path)
        
        # Create directories if they don't exist
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return os.path.join(asset_folder, path)
    except requests.RequestException as e:
        print(f"Error downloading {url}: {str(e)}")
    except OSError as e:
        print(f"Error saving {url} to {local_path}: {str(e)}")
    return url

def scrape_and_save(url, selector, output_file, asset_folder='assets'):
    try:
        # Create base directory
        base_path = os.path.dirname(os.path.abspath(output_file))
        os.makedirs(base_path, exist_ok=True)
        
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
                local_path = download_resource(absolute_url, base_path, asset_folder)
                if local_path.startswith(asset_folder):
                    elem[attr] = os.path.relpath(local_path, os.path.dirname(output_file))
        
        # Save modified HTML
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(selected_element))
        
        print(f"Successfully saved content to {output_file}")
    except requests.RequestException as e:
        print(f"Error fetching {url}: {str(e)}")
    except OSError as e:
        print(f"Error creating directories or saving file: {str(e)}")
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python scrape_content.py <url> <css_selector> <output_file>")
        sys.exit(1)
    
    scrape_and_save(sys.argv[1], sys.argv[2], sys.argv[3])