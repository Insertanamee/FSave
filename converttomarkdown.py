import os
import markdownify
from markdownify import MarkdownConverter

class CustomMarkdownConverter(MarkdownConverter):
    def convert_sub(self, el, text, parent_tags):
        return f"<sub>{text}</sub>"

    def convert_sup(self, el, text, parent_tags):
        return f"<sup>{text}</sup>"

    def convert_b(self, el, text, parent_tags):
        return f"<b>{text}</b>"

    def convert_i(self, el, text, parent_tags):
        return f"<i>{text}</i>"
    
    def convert_u(self, el, text, parent_tags):
        return f"<u>{text}</u>"

    def convert_s(self, el, text, parent_tags):
        return f"<s>{text}</s>"
    
    def convert_math(self, el, text, parent_tags):
        return f"<math>{text}</math>"

def custom_markdownify(html, **options):
    return CustomMarkdownConverter(**options).convert(html)

def convert_html_to_md(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_file_path = os.path.join(root, file)
                md_file_path = os.path.splitext(html_file_path)[0] + '.md'
                
                with open(html_file_path, 'r', encoding='utf-8') as html_file:
                    html_content = html_file.read()
                
                md_content = custom_markdownify(html_content)
                
                with open(md_file_path, 'w', encoding='utf-8') as md_file:
                    md_file.write(md_content)
                
                os.remove(html_file_path)  # Delete the original HTML file
                print(f"Converted {html_file_path} to {md_file_path} and deleted the original HTML file")

if __name__ == "__main__":
    directory = "a-level"
    convert_html_to_md(directory)