import os
import markdownify

def convert_html_to_md(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_file_path = os.path.join(root, file)
                md_file_path = os.path.splitext(html_file_path)[0] + '.md'
                
                with open(html_file_path, 'r', encoding='utf-8') as html_file:
                    html_content = html_file.read()
                
                md_content = markdownify.markdownify(html_content, heading_style="ATX")
                
                with open(md_file_path, 'w', encoding='utf-8') as md_file:
                    md_file.write(md_content)
                
                os.remove(html_file_path)  # Delete the original HTML file
                print(f"Converted {html_file_path} to {md_file_path} and deleted the original HTML file")

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    convert_html_to_md(directory)