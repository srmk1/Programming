import imaplib
from email.message import Message
from time import time

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "GMAIL_ID_HERE" + ORG_EMAIL
FROM_PWD    = "PWD_HERE"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def login_to_gmail(user_name, password):
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        return mail
    except Exception:
        print(str(Exception))

def send_message(mail):
    new_message = Message()
    new_message["From"] = "srmkcloudapps@gmail.com"
    new_message["Subject"] = "My new mail."
    new_message.set_payload("This is my message.")
    mail.append('INBOX', '', imaplib.Time2Internaldate(time()), str(new_message).encode('utf-8'))


my_gmail = login_to_gmail(FROM_EMAIL,FROM_PWD)
send_message(my_gmail)
