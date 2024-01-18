import os
import shutil

def organize_files(source_folder):
    # Define destination folders
    document_folder = os.path.join(source_folder, "Documents")
    image_folder = os.path.join(source_folder, "Images")
    video_folder = os.path.join(source_folder, "Videos")
    other_folder = os.path.join(source_folder, "Other")

    # Create destination folders if they don't exist
    for folder in [document_folder, image_folder, video_folder, other_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # List all files in the source folder
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    # Organize files based on file type
    for file in files:
        file_path = os.path.join(source_folder, file)

        # Determine the file type
        file_type = file.split('.')[-1].lower()

        # Move the file to the appropriate folder
        if file_type in ['doc', 'docx', 'txt', 'pdf']:
            shutil.move(file_path, os.path.join(document_folder, file))
        elif file_type in ['jpg', 'jpeg', 'png', 'gif']:
            shutil.move(file_path, os.path.join(image_folder, file))
        elif file_type in ['mp4', 'avi', 'mkv']:
            shutil.move(file_path, os.path.join(video_folder, file))
        else:
            shutil.move(file_path, os.path.join(other_folder, file))

    print("File organization complete.")

# Example usage:
source_directory = "/path/to/source/directory"
organize_files(source_directory)

