from configparser import ConfigParser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class EmailSender:
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

    def message_sending(self, recipient: str, subject: str, message: str, attachment_path: str):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        # Attach the image
        try:
            with open(attachment_path, 'rb') as attachment:
                mime_base = MIMEBase('application', 'octet-stream')
                mime_base.set_payload(attachment.read())
                encoders.encode_base64(mime_base)
                mime_base.add_header('Content-Disposition',
                                     f'attachment; filename={attachment_path}')
                msg.attach(mime_base)
        except FileNotFoundError:
            print(f"Attachment file not found at {attachment_path}")
            return

        # Send the email
        self.send_mail(self.email, self.password, recipient, msg)

    def send_mail(self, email, password, recipient, msg):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, recipient, msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
        finally:
            server.quit()


config = ConfigParser()
config.read('cred.ini')
password = config['stelth_attack']['Attack_KEY']

sender = EmailSender("adittyanarayan77@gmail.com", password)


def sendEmail(imagePath, receiverEmail, userid):
    sender.message_sending(
        recipient=receiverEmail,
        subject="Welcome to the organization!",
        message=f"Here is Your UserId: {userid} and your Credential Private Image is in the attachment.",
        attachment_path=imagePath
    )
