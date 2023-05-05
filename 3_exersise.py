import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class Mailer():
    def __init__(self, user_login, user_password, GMAIL_SMTP="smtp.gmail.com", GMAIL_IMAP="imap.gmail.com"):
        self.user_login = user_login
        self.user_password = user_password
        self.GMAIL_SMTP = GMAIL_SMTP
        self.GMAIL_IMAP = GMAIL_IMAP

    def send_massage(self, recipients: list, subject: str, message: str):
        msg = MIMEMultipart()
        msg['From'] = self.user_login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        ms = smtplib.SMTP(self.GMAIL_SMTP, 587)  # identify ourselves to smtp gmail client
        ms.ehlo()  # secure our email with tls encryption
        ms.starttls()  # re-identify ourselves as an encrypted connection
        ms.ehlo()
        ms.login(self.user_login, self.user_password)
        ms.sendmail(self.user_login, ms, msg.as_string())
        ms.quit()

    def receive_message(self, header=None):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.user_login, self.user_password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
