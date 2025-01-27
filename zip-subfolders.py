import os
import zipfile

# Specify the root folder containing the subfolders
root_folder = "/root/folder/here"

# Process only the direct subfolders of the root folder
for folder_name in os.listdir(root_folder):
  subdir = os.path.join(root_folder, folder_name)

  # Check if it's a folder (and not a file)
  if not os.path.isdir(subdir):
    continue

  # Define the output zip file path
  zip_file_path = os.path.join(root_folder, f"{folder_name}.zip")

  # Create a zip file for the subfolder
  with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Add all files and subfolders inside the subdir to the zip file
    for root, _, sub_files in os.walk(subdir):
      for file in sub_files:
        file_path = os.path.join(root, file)
        # Preserve relative folder structure
        arcname = os.path.relpath(file_path, subdir)
        zipf.write(file_path, arcname)
        
  print(f"Zipped folder: {subdir} -> {zip_file_path}")
