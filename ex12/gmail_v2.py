import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

#APP PASSWD
def send_email_with_attachment(subject, body, to_email, from_email, from_email_password, file_path):
    # Create the MIMEMultipart object
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body text to the email
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file to the email
    if os.path.exists(file_path):
        with open(file_path, 'rb') as attachment:
            # Create a MIMEBase object and set the appropriate headers
            file_name = os.path.basename(file_path)
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={file_name}')
            msg.attach(part)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, from_email_password)
        server.sendmail(from_email, to_email, msg.as_string())
        print(f"Email sent to {to_email} with attachment {file_path}.")

if __name__ == '__main__':
    subject = 'NO ONE THOUGHT IT WAS POSSIBLE'
    body = '🦛🦛🦛🦛🦛🦛🦛🦛🦛🦛🦛🦛🦛'
    to_email = 'mkaradeniz2003@gmail.com'
    from_email = 'SeniorPromptEngineer@gmail.com'
    from_email_password = 'wfazpkqfxwzzsgwa'
    file_path = '/Users/mkaraden/Desktop/cokgizli.txt'

    send_email_with_attachment(subject, body, to_email, from_email, from_email_password, file_path)
