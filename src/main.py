import os
import shutil

from copystaticdir import copy_files_recursive
from generatepage import generate_page


path_to_static = "../static"
path_to_public = "../public"

def main():
    print("Deleting public directory...")
    if os.path.exists(path_to_public):
        shutil.rmtree(path_to_public, ignore_errors=True)
        print("Public directory deleted.")
    else:
        print("Public directory does not exist.")
    
    print("Copying static files to public directory...")
    copy_files_recursive(path_to_static, path_to_public)
    generate_page( 
        "../content/index.md",
        "../template.html",
        os.path.join(path_to_public, "index.html")
    )

main()     