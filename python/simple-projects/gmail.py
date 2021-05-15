import imaplib
import email
import os
import datetime
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.disable(logging.INFO)
# -------------------------------------------------
# Logging Module
# Logging levels
# logging.debug() - Lowest level
# logging.info()
# logging.warning()
# logging.error()
# logging.critical() - highest level
#
# You can disable logging using
# logging.disable(logging.CRITICAL)
# at the beginning of the file
#
# Writing log to a file:
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' \
# %(asctime)s - %(levelname)s - %(message)s')
# -------------------------------------------------

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# Note that you need to use app-passwords.
# If you want to avoid this error without compromising your account's security, use OAuth to authenticate. 
# The protocol is documented here, and there is Python sample code that shows the use of XOAUTH2 with imaplib.
# Independent of this, you should consider enabling two-step verification on your account to make it more secure. 
# If you do, you can use an App Password to connect to IMAP, which might also avoid the above warning.
#
# SIGIN TO GMAIL USING APP PASSWORDS
# https://support.google.com/accounts/answer/185833?hl=en
# ------------------------------------------------
ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "yourid" + ORG_EMAIL
FROM_PWD    = "app-password"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993
SEARCH_FILTER = '(FROM "NSDL" SUBJECT "Your NSDL CAS - *")'

def download_attachment(msg, download_folder):
    try:
        # Check for attachments
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            filename = part.get_filename()
            logging.debug(filename)

            # Download the attachment to the directory
            att_path = os.path.join(download_folder, filename)
            if not os.path.isfile(att_path):
                fp = open(att_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
    except Exception:
        print(str(Exception))


def print_msg(msg, is_print=False):
    if is_print:
        print_headers(msg)
        print_msg_text(msg)


def print_headers(msg):
    email_subject = msg['subject']
    email_from = msg['from']
    email_to = msg['to']
    email_date = msg['date']

    print(msg.items())
    print('From : ' + email_from)
    print('To : ' + email_to)
    print('Subject : ' + email_subject)
    print('Date :' + email_date + "\n")


def print_msg_text(msg):
    maintype = msg.get_content_maintype()
    if maintype == 'multipart':
        for part in msg.get_payload():
            if part.get_content_maintype() == 'text':
                print(part.get_payload())
    elif maintype == 'text':
        print(msg.get_payload())


def login_to_gmail(user_name, password):
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        return mail
    except Exception:
        print(str(Exception))


def search_email_inbox(mail, search_filter, is_download=False, download_folder=""):
    try:
        mail.select('inbox')
        type, data = mail.search(None, search_filter)
        mail_ids = data[0]
        print(data[0])
        id_list = mail_ids.split()

        for i in id_list:
            typ, data = mail.fetch(i, '(RFC822)')
            for response_part in data:
                logging.debug(response_part)
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1].decode('utf-8'))
                    print_msg(msg, False)
                    if is_download == True:
                        download_attachment(msg, download_folder)
    except Exception:
        print(str(Exception))


def search_email_since_pastday(mail, is_download=False, download_folder=""):
    try:
        mail.select('inbox')
        date = (datetime.date.today() - datetime.timedelta(1)).strftime("%d-%b-%Y")
        type, data = mail.search(None, '(SENTSINCE {date})'.format(date=date))

        mail_ids = data[0]
        print(data[0])

        id_list = mail_ids.split()
        for i in id_list:
            typ, data = mail.fetch(i, '(RFC822)')
            for response_part in data:
                logging.debug(response_part)
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1].decode('utf-8'))
                    print_msg(msg, False)
                    if is_download == True:
                        download_attachment(msg, download_folder)
            break
    except Exception:
        print(str(Exception))


mail = login_to_gmail(FROM_EMAIL, FROM_PWD)
#search_email_inbox(mail, SEARCH_FILTER)
#search_email_since_pastday(mail)
