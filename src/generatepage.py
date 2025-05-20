import os
import stat
from markdown_blocks import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    """
    Generates a page by copying a template and replacing placeholders with content.
    
    Args:
        from_path (str): Path to the source file.
        template_path (str): Path to the template file.
        dest_path (str): Path to the destination file.
    """
    print(f"Absolute paths:")
    print(f"From: {os.path.abspath(from_path)}")
    print(f"Template: {os.path.abspath(template_path)}")
    print(f"Destination: {os.path.abspath(dest_path)}")

    if os.path.isfile(from_path) and os.path.isfile(template_path):
        print(f"Generating page from {from_path} to {dest_path} using template {template_path}")       
        print(f"Attempting to read file from: {from_path}")
        try:
            with open(from_path, "r") as source_file:
                content = source_file.read()
            print(f"Successfully read {len(content)} characters")
        except Exception as e:
            print(f"Error reading file: {e}")
        
        content_title = extract_title(content)
        content_node = markdown_to_html_node(content)
        content_html = content_node.to_html()      

    # Replace placeholders in the template with actual content
        with open(template_path, "r") as template_file:
            template = template_file.read()        
        new_page = template.replace("{{ Title }}", content_title)
        new_page = new_page.replace("{{ Content }}", content_html)

    # Write the generated page to the destination path
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        try:
            with open(dest_path, "w") as dest_file:
                dest_file.write(new_page)
            print(f"Successfully wrote page to {dest_path}")
        except Exception as e:
            print(f"Error writing file to {dest_path}: {e}")
   
    else:
        print(f"Source file {from_path} or template file {template_path} does not exist.")
        return   

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively generates pages for all markdown files in a directory.
    
    Args:
        dir_path_content (str): Path to the directory containing markdown files.
        template_path (str): Path to the template file.
        dest_dir_path (str): Path to the destination directory.
    """
    if not os.path.exists(dir_path_content):
        print(f"Directory {dir_path_content} does not exist.")
        return
    
    print(f"Generating pages recursively in {dir_path_content} using template {template_path} to {dest_dir_path}") 
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, dir_path_content)
                dest_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + ".html")
                generate_page(from_path, template_path, dest_path)




