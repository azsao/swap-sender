import os
import subprocess
from time import sleep

referencepp_directory = "reference++"
scripts_directory = "scripts"

def check_directories_exist():
    referencepp_exists = os.path.exists(referencepp_directory)
    scripts_exists = os.path.exists(scripts_directory)

    print(f'Directory "{referencepp_directory}" exists: {referencepp_exists}')
    print(f'Directory "{scripts_directory}" exists: {scripts_exists}')

sleep(2)

if __name__ == "__main__":
    check_directories_exist()

    # Run the mover script
    mover_path = 'scripts/mover.py'
    try:
        subprocess.run(['python', mover_path], check=True)
        print(f"Script '{mover_path}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing script '{mover_path}': {e}")

    # Run the name script
    name_path = 'scripts/name.py'
    try:
        subprocess.run(['python', name_path], check=True)
        print(f"Script '{name_path}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing script '{name_path}': {e}")

    # Run the sender script
    sender_path = 'scripts/sender.py'
    try:
        subprocess.run(['python', sender_path], check=True)
        print(f"Script '{sender_path}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing script '{sender_path}': {e}")
