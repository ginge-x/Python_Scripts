import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Conor Irwin'
email['to'] = 'conorirwin1@icloud.com'
email['Subject'] = 'You won £1000'

email.set_content(html.substitute(name='TinTin'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('conorirwin2004@gmail.com', 'adot ezvl vtii myvu')
    smtp.send_message(email)
    print('all good boss!')