from smtplib import SMTP_SSL, SMTP_SSL_PORT

# Generate app password using below link
# https://myaccount.google.com/apppasswords
SMTP_HOST = 'smtp.gmail.com'
SMTP_USER = 'GMAIL_HERE@gmail.com'
SMTP_PASS = 'PWD_HERE'

# Craft the email by hand
from_email = 'srmkcloudapps@gmail.com'  # or simply the email address
to_emails = ['srikanth.mk@gmail.com']
body = "Hello, world!"
headers = f"From: {from_email}\r\n"
headers += f"To: {', '.join(to_emails)}\r\n"
headers += f"Subject: Hello\r\n"
email_message = headers + "\r\n" + body  # Blank line needed between headers and body

# Connect, authenticate, and send mail
smtp_server = SMTP_SSL(SMTP_HOST, port=SMTP_SSL_PORT)
smtp_server.set_debuglevel(1)  # Show SMTP server interactions
smtp_server.login(SMTP_USER, SMTP_PASS)
smtp_server.sendmail(from_email, to_emails, email_message)

# Disconnect
smtp_server.quit()
