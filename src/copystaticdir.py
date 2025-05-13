import os
import shutil


def copy_files_recursive(source_path, dest_path):
    if not os.path.exists(dest_path):
        print(f"Creating directory: {dest_path}")
        os.mkdir(dest_path)

    for filename in os.listdir(source_path):
        from_path = os.path.join(source_path, filename)
        dest_path = os.path.join(dest_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)