import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(sender_email, sender_password, receiver_email, subject, body, files):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Attach files
    for file in files:
        with open(file, 'rb') as attachment:
            part = MIMEApplication(attachment.read())
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file)}')
            message.attach(part)

    # Connect to the SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == "__main__":
    # Update these values with your email and SMTP server details
    sender_email = "example@gmail.com"
    sender_password = "exampletext" #enter the app password here
    receiver_email = "example@gmail.com"
    subject = "This is an example message"
    body = "This is an example body message, shoutout the homie 0sric"

    # Update this path to the directory containing the files you want to send
    selected_path = r"C:/Path/To/Selected/Directory"

    # Get a list of files in the directory
    files_to_send = [os.path.join(selected_path, file) for file in os.listdir(selected_path) if os.path.isfile(os.path.join(selected_path, file))]

    # Send the email
    send_email(sender_email, sender_password, receiver_email, subject, body, files_to_send)
