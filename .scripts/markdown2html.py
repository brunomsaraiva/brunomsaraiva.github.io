import markdown
import os

def convert_markdown_to_html(input_file, output_file):
    # Read the markdown file
    with open(input_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
    
    # Convert markdown to html
    html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite', 'toc'])

    # Write the html content to the output file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":

    base_path = "../"
    markdown_path = base_path + os.sep + ".markdown"

    for filename in os.listdir(markdown_path):
        if filename.endswith(".md"):
            input_file = markdown_path + os.sep + filename
            output_file = base_path + os.sep + filename.replace(".md", ".html")
            convert_markdown_to_html(input_file, output_file)
