import os

def list_files_and_folders(path, indent=0):
    for entry in sorted(os.listdir(path)):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            print('  ' * indent + f"[FOLDER] - {entry}")
            list_files_and_folders(full_path, indent + 1)
        else:
            print('  ' * indent + f"[FILE] - {entry}")

if __name__ == "__main__":
    start_path = os.path.dirname(os.path.abspath(__file__))
    print(f"Listing files and folders in: {start_path}\n")
    list_files_and_folders(start_path)
