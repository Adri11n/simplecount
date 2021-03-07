import sys
import smtplib
import ssl

counter = sys.argv[1]
smtp_server = sys.argv[2]
sender_email = sys.argv[3]
port = int(sys.argv[4])
receiver_email = sys.argv[5]
password = sys.argv[6]

with open(counter + ".txt", "r") as database:
    value = database.read()
message = f"""\
Subject: Here is the exported value of you simplecount counter {counter}

The value of your counter is {value}."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)