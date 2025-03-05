import argparse
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

def extract_links(url, output_file='links.txt'):
    """Extract and process links from a webpage"""
    try:
        # Fetch webpage content
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse base URL
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Find target section using CSS selector
        target_section = soup.select_one('div.gy-4:nth-child(1)')
        if not target_section:
            print("Target section not found in the page")
            return

        # Extract and process links
        links = []
        for a in target_section.find_all('a', href=True):
            href = a['href']
            # Convert relative URLs to absolute
            full_url = urljoin(base_url, href)
            links.append(full_url)

        # Save to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(links))
            
        print(f"Successfully extracted {len(links)} links to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Extract links from specific section of a webpage'
    )
    parser.add_argument('url', help='URL to analyze')
    parser.add_argument('-o', '--output', help='Output file name', default='links.txt')
    args = parser.parse_args()

    extract_links(args.url, args.output)