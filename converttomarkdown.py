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
    
    def convert_mi(self, el, text, parent_tags):
        return f"<mi>{text}</mi>"
    
    def convert_mo(self, el, text, parent_tags):
        return f"<mo>{text}</mo>"
    
    def convert_mn(self, el, text, parent_tags):
        return f"<mn>{text}</mn>"
    
    def convert_mtext(self, el, text, parent_tags):
        return f"<mtext>{text}</mtext>"
    
    def convert_mrow(self, el, text, parent_tags):
        return f"<mrow>{text}</mrow>"
    
    def convert_mfrac(self, el, text, parent_tags):
        return f"<mfrac>{text}</mfrac>"
    
    def convert_mroot(self, el, text, parent_tags):
        return f"<mroot>{text}</mroot>"
    
    def convert_msub(self, el, text, parent_tags):
        return f"<msub>{text}</msub>"
    
    def convert_msup(self, el, text, parent_tags):
        return f"<msup>{text}</msup>"
    
    def convert_msubsup(self, el, text, parent_tags):
        return f"<msubsup>{text}</msubsup>"
    
    def convert_munder(self, el, text, parent_tags):
        return f"<munder>{text}</munder>"
    
    def convert_mover(self, el, text, parent_tags):
        return f"<mover>{text}</mover>"
    
    def convert_munderover(self, el, text, parent_tags):
        return f"<munderover>{text}</munderover>"
    
    def convert_mtable(self, el, text, parent_tags):
        return f"<mtable>{text}</mtable>"
    
    def convert_mtr(self, el, text, parent_tags):
        return f"<mtr>{text}</mtr>"
    
    def convert_mtd(self, el, text, parent_tags):
        return f"<mtd>{text}</mtd>"
    
    def convert_mth(self, el, text, parent_tags):
        return f"<mth>{text}</mth>"
    
    def convert_merror(self, el, text, parent_tags):
        return f"<merror>{text}</merror>"
    
    def convert_mspace(self, el, text, parent_tags):
        return f"<mspace>{text}</mspace>"
    
    def convert_mphantom(self, el, text, parent_tags):
        return f"<mphantom>{text}</mphantom>"
    
    def convert_mfenced(self, el, text, parent_tags):
        return f"<mfenced>{text}</mfenced>"
    
    def convert_menclose(self, el, text, parent_tags):
        return f"<menclose>{text}</menclose>"
    
    def convert_maction(self, el, text, parent_tags):
        return f"<maction>{text}</maction>"
    
    def convert_maligngroup(self, el, text, parent_tags):
        return f"<maligngroup>{text}</maligngroup>"
    
    def convert_malignmark(self, el, text, parent_tags):
        return f"<malignmark>{text}</malignmark>"
    
    def convert_mglyph(self, el, text, parent_tags):
        return f"<mglyph>{text}</mglyph>"
    
    def convert_semantics(self, el, text, parent_tags):
        return f"<semantics>{text}</semantics>"
    
    def convert_annotation(self, el, text, parent_tags):
        return f"<annotation>{text}</annotation>"

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