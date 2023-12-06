import os
import random
from datetime import datetime
from time import sleep


def rename_files(directory_path):
    # Get a list of all files in the directory
    files = os.listdir(directory_path)

    # Iterate through each file in the directory
    for file_name in files:
        # Generate the new name
        new_name = generate_new_name()

        # Construct the full paths for the old and new names
        old_path = os.path.join(directory_path, file_name)
        new_path = os.path.join(directory_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f'Renamed: {file_name} to {new_name}')

print("Getting ready to rename, holding....")
sleep (2)

def generate_new_name():
    # Get the current date in the format YYYYMMDD
    date_str = datetime.now().strftime("%Y%m%d")

    # Generate two random numbers between 10 and 99
    random_number1 = random.randint(10, 99)
    random_number2 = random.randint(10, 99)

    # Construct the new name
    new_name = f'[{date_str}]Instagram-Video[{random_number1}{random_number2}]'

    return new_name


# Specify the directory path
directory_path = r'reference++\selected'

# Call the function to rename files in the specified directory
rename_files(directory_path)
