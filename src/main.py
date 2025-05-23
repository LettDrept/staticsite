import os
import shutil
import sys

from copystaticdir import copy_files_recursive
from generatepage import generate_page, generate_pages_recursive

def main():
# Check if a basepath is provided as a command line argument, otherwise uses "/" for the root
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    if basepath[-1] != "/":
        basepath += "/"
    print(f"Basepath: {basepath}")

# Get the directory containing your script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
# Navigate up one level if needed (depending on your project structure)
    base_dir = os.path.dirname(script_dir)  # or just script_dir if main.py is at the root
    
# Construct absolute paths
    content_path = os.path.join(base_dir, "content")   # Needed "index.md" for only one page
    template_path = os.path.join(base_dir, "template.html")
    if basepath == "/":
        public_dir = os.path.join(base_dir, "public")
    else:
        public_dir = os.path.join(base_dir, "docs")
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
    generate_page(content_path, template_path, public_index_path, basepath)

# Generate pages recursively
    generate_pages_recursive(content_path, template_path, public_dir, basepath)

if __name__ == "__main__":
    main()   