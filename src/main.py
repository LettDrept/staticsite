import os
import shutil

from copystaticdir import copy_files_recursive
from generatepage import generate_page

def main():
# Get the directory containing your script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
# Navigate up one level if needed (depending on your project structure)
    base_dir = os.path.dirname(script_dir)  # or just script_dir if main.py is at the root
    
# Construct absolute paths
    content_path = os.path.join(base_dir, "content", "index.md")
    template_path = os.path.join(base_dir, "template.html")
    public_dir = os.path.join(base_dir, "public")
    public_index_path = os.path.join(public_dir, "index.html")
    static_dir = os.path.join(base_dir, "static")
    
    print(f"Content path: {content_path}")
    print(f"Template path: {template_path}")
    print(f"Public dir: {public_dir}")
    print(f"Public index path: {public_index_path}")
    print(f"Static dir: {static_dir}")
    
# Delete public directory
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir, ignore_errors=True)
        print("Public directory deleted.")
    
# Create public directory
    os.makedirs(public_dir, exist_ok=True)
    print("Public directory created.")
    
# Copy static files
    if os.path.exists(static_dir):
        copy_files_recursive(static_dir, public_dir)
        print(f"Copied static files from {static_dir} to {public_dir}")
    
# Generate page
    generate_page(content_path, template_path, public_index_path)

if __name__ == "__main__":
    main()   