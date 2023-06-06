import os
import zipfile

model_folder = "model"
output_zip = "doggy.zip"
this_folder = "."
variables = f"{model_folder}/variables"
variables_zip = f"{variables}/variables.zip"
with zipfile.ZipFile(f"{variables_zip}", 'r') as zip_ref:
    zip_ref.extractall(variables)

exclude_file_types = [output_zip, "variables.zip"]
exclude_folders = ["venv", "__pycache__", ".git", ".idea"]

current_dir = os.getcwd()
files_to_zip = []
for root, dirs, files in os.walk(current_dir):
    dirs[:] = [d for d in dirs if d not in exclude_folders]
    files = [f for f in files if not any(f.endswith(ext) for ext in exclude_file_types)]
    for file in files:
        file_path = os.path.join(root, file)
        files_to_zip.append(file_path)

with zipfile.ZipFile(output_zip, 'w') as zip_file:
    for file in files_to_zip:
        arcname = os.path.relpath(file, current_dir)
        zip_file.write(file, arcname)

print("Files zipped successfully.")