#!/usr/bin/env python3

from os import getenv
import smtplib

email = getenv("EMAIL")
password = getenv("PWD")

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email, password)

    subject = "SMTP Check 1,2"
    body = "I wonder if we could have done it like this all along"

    msg = f"Subject: {subject} \n\n{body}"

    smtp.sendmail(email, "havemercyonmike@yahoo.com", msg)

print("Email sent")
