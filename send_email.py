import smtplib
from email.message import EmailMessage

from_email_addr = "REPLACE_WITH_THE_SENDER_EMAIL"
from_email_pass = "REPLACE_WITH_THE_SENDER_EMAIL_APP_PASSWORD"
to_email_addr = "REPLACE_WITH_THE_RECIPIENT_EMAIL"

msg = EmailMessage()

body = "Hello from Raspberry Pi"
msg.set_content(body)

msg['From'] = from_email_addr
msg['To'] = to_email_addr
msg['Subject'] = 'TEST EMAIL'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
