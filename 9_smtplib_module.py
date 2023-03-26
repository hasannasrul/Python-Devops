import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# create a message object instance
message = MIMEMultipart()

# Email body
body = 'This is a sample email from python with attachment'
message.attach(MIMEText(body, 'plain'))

# Attachment
with open(os.path.join(os.getcwd(),'Scripts','logs.csv')) as attachment:
    part = MIMEApplication(attachment.read(), Name='logs.csv')
    part['Content-Disposition'] = 'attachment; filename="logs.csv"'
    message.attach(part)

# Email header
message['From'] = "hasanali242424@gmail.com"
message['To'] = "hasanali50923@gmail.com"
message['Subject'] = "Python Devops - SMTP Module "

# Smtp server
smtp_server = os.environ.get('SMTP_SERVER')
smtp_port = os.environ.get('SMTP_PORT')

# start TLS encryption
smtp_server = smtplib.SMTP(smtp_server,smtp_port)
smtp_server.starttls()

# Login to smtp server
smtp_server.login('hasanali242424@gmail.com', os.environ.get('GMAIL_APP_PASSWORD'))

# Send email
smtp_server.sendmail(message['From'], message['To'], message.as_string())

# close SMTP server connection 
smtp_server.quit()