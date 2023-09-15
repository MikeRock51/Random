#!/usr/bin/env python3

from os import getenv
import smtplib
from email.message import EmailMessage

email = getenv("EMAIL")
password = getenv("PWD")
msg = EmailMessage()
msg['Subject'] = "Think and Grow Rich"
msg['From'] = email
msg['To'] = "mikerockmusic51@gmail.com"
msg.set_content("Count down 5...4...3...2...1..")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email, password)
    smtp.send_message(msg)

print("Email sent")
