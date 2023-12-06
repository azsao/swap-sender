# Swap Sender Repository

Welcome to the Swap Sender repository! This repository provides Python scripts to facilitate file management and email notifications. The primary features include moving files between directories and sending email notifications with attachments.
File Mover (mover.py)
move_all_files(source_path, destination_path)

This function efficiently moves all files from the source directory to the specified destination directory.

    Parameters:
        source_path: Path to the source directory.
        destination_path: Path to the destination directory.

select_and_move_files(source_path, destination_path, num_files=2)

This function randomly selects a user-defined number of files from the source directory and relocates them to the destination directory.

    Parameters:
        source_path: Path to the source directory.
        destination_path: Path to the destination directory.
        num_files: Number of files to be randomly selected (default is 2).

Email Sender (sender.py)
send_email(sender_email, sender_password, receiver_email, subject, body, files)

This function sends an email with attachments using specified SMTP server details.

    Parameters:
        sender_email: Sender's email address.
        sender_password: App password for the sender's email account.
        receiver_email: Recipient's email address.
        subject: Subject of the email.
        body: Body of the email.
        files: List of file paths to be attached to the email.

Getting Started

    Configuration:
        Adjust the source and destination paths in mover.py according to your directory structure.
        Update sender, receiver, and SMTP server details in sender.py.

    File Mover:
        Execute execute.py to move files between directories.

    Email Sender:
        Set the directory containing files to be sent by updating the selected_path variable in sender.py.

Note: Ensure that you have the necessary permissions and configurations, such as enabling apps password for Gmail, to use the email sender functionality.

Feel free to customize and integrate these scripts into your projects. For any issues or improvements, please open an issue or contribute to the development of this repository. 
