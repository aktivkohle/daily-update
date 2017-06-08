import config
import smtplib
from email.mime.text import MIMEText
from smtplib import SMTP_SSL as SMTP

username = config.GMAIL_ADDR
password = config.GMAIL_PWD

def sendresult(text):        
    msg = MIMEText(text)
    msg['Subject'] = config.SUBJECT 
    me = username
    msg['From'] = me
    msg['To'] = ", ".join(config.TO)
    conn = SMTP('smtp.gmail.com:465')
    conn.set_debuglevel(True)
    conn.login(username, password)
    conn.send_message(msg)
    conn.close()
