import os
import random
import shutil
from time import sleep

def move_all_files(source_path, destination_path):
    # Get a list of all files in the source directory
    all_files = os.listdir(source_path)

    # Move all files to the destination directory
    for file_name in all_files:
        source_file_path = os.path.join(source_path, file_name)
        destination_file_path = os.path.join(destination_path, file_name)

        # Move the file
        shutil.move(source_file_path, destination_file_path)
        print(f'Moved: {file_name}')

if __name__ == "__main__":
    # Define source and destination paths
    selected_path = r'reference++\selected'
    used_path = r'reference++\used'

    # Ensure the destination directory exists
    os.makedirs(used_path, exist_ok=True)

    # Move all files from "selected" to "used"
    move_all_files(selected_path, used_path)

    sleep(4)

def select_and_move_files(source_path, destination_path, num_files=2):
    # Get a list of all files in the source directory
    all_files = os.listdir(source_path)

    # Randomly select num_files files
    selected_files = random.sample(all_files, min(num_files, len(all_files)))

    # Move selected files to the destination directory
    for file_name in selected_files:
        source_file_path = os.path.join(source_path, file_name)
        destination_file_path = os.path.join(destination_path, file_name)

        # Move the file
        shutil.move(source_file_path, destination_file_path)
        print(f'Moved: {file_name}')

        sleep(2)

if __name__ == "__main__":
    # Define source and destination paths
    unselected_path = r'reference++\unselected'
    selected_path = r'reference++\selected'

    # Ensure the destination directory exists
    os.makedirs(selected_path, exist_ok=True)

    # Select and move 2 files
    select_and_move_files(unselected_path, selected_path, num_files=2)
