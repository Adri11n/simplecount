import sys
import smtplib
import ssl
which = sys.argv[1]
counter = sys.argv[2]
smtp_server = sys.argv[3]
sender_email = sys.argv[4]
port = int(sys.argv[5])
receiver_email = sys.argv[6]
password = sys.argv[7]

if which == "value":
    with open(counter + ".txt", "r") as database:
        value = database.read()
    message = f"""\
Subject: Here is the exported value of your simplecount counter {counter}

The value of your counter is {value}."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
elif which == "log":
    with open("simplecount.log", "r") as database:
        value = database.read()
    message = f"""\
Subject: Here is the exported log of your simplecount log

{value}."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)