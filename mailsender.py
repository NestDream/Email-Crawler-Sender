#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mailsender.py
@Time    :   2019/01/21 23:34:10
@Author  :   Li Guo 
@Version :   1.0
@Contact :  gl_1997@outlook.com
@License :   Copyright (c) 2019 Li Guo
@Desc    :   None
'''

# Imported libs

import email

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from email.mime.image import MIMEImage

from email.mime.base import MIMEBase

import smtplib
import time

sender = username = '' # your email address
userpwd = '' #your email password
host = 'smtp.163.com'
port = 25

# extract emails to send from a txt file
recipients = []

with open('allmail.txt', 'r+', encoding='utf-8') as file:
    for i in file.readlines():
        recipients.append(i.strip())

recipients = tuple(recipients)

# log in 

server = smtplib.SMTP(host, port)

server.starttls()

server.login(username, userpwd)

# begin to send

count = 0

for recipient in recipients:
    # creat your email

    msg = MIMEMultipart()

    msg.set_charset('utf-8')


    msg['Reply-to'] = 'python_nku_bc@163.com'

    # set the header of the email

    msg.add_header('From', sender)

    msg.add_header('To', recipient)

    msg.add_header('Subject', recipient.split('@')[0] + ', Happy New Year!')

    # set the content of the email
    body = '''Dear ''' + recipient.split('@')[
        0] + ''',\n\t2019 has come, Happy New Year!\n\tBuilding a high-rise begins with mounds of soil. Let's work hard together to build a better future!\nObama,\nNankai University'''
    msg.attach(MIMEText(body, 'plain', _charset="utf-8"))

    # send them now! It would be better if you send them in a proper frequency, below is an example

    server.send_message(msg)
    print(body)
    time.sleep(10)
    count = count + 1
    if count == 11:
        server.quit()
        time.sleep(120)
        server = smtplib.SMTP(host, port)
        server.starttls()
        server.login(username, userpwd)
        count = 0

# quit the sever

server.quit()
