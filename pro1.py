import os
import shutil

# Define where files should go
DIRECTORY = "./TargetFolder"
FOLDERS = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Archives": [".zip", ".rar"]
}

def organize():
    for filename in os.listdir(DIRECTORY):
        filepath = os.path.join(DIRECTORY, filename)
        if os.path.isdir(filepath): continue
        
        ext = os.path.splitext(filename)[1].lower()
        for folder, extensions in FOLDERS.items():
            if ext in extensions:
                dest_folder = os.path.join(DIRECTORY, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(filepath, os.path.join(dest_folder, filename))
                print(f"Moved {filename} to {folder}")

if __name__ == "__main__":
    organize()