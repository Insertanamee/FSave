import os
from urllib.parse import urlparse

# Configuration
INPUT_FILE = 'links.txt'
CONSTANT = "div.row.g-4"  # ← Replace with your actual constant value

def execute_commands():
    try:
        with open(INPUT_FILE, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]

        success_count = 0
        failure_count = 0

        for url in urls:
            try:
                # Parse URL and extract path
                parsed = urlparse(url)
                path_segment = parsed.path.lstrip('/')
                
                if not path_segment:
                    path_segment = 'root'

                # Create and execute command
                cmd = f'python scrape_content.py "{url}" "{CONSTANT}" "{path_segment}"'
                print(f"Executing: {cmd}")
                
                # Run command and check result
                result = os.system(cmd)
                
                if result == 0:
                    success_count += 1
                else:
                    failure_count += 1
                    print(f"Command failed for URL: {url} (Error code: {result})")

            except Exception as e:
                print(f"Error processing {url}: {str(e)}")
                failure_count += 1

        print(f"\nExecution summary:")
        print(f"Successfully processed: {success_count}")
        print(f"Failed: {failure_count}")

    except FileNotFoundError:
        print(f"Error: Missing {INPUT_FILE} - run the previous script first")
    except Exception as e:
        print(f"Critical error: {str(e)}")

if __name__ == "__main__":
    execute_commands()