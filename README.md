# simplecount
if you need help with the args run the file and type
```
help
```
# export feature
with this feature you can export counter values and your hole logfile using email.
the script must be startet like this
```
#on Linux
python3 export.py
#on windows
python export.py
```
#Arguments that are nedded for export.py
this is the lis of arguments
```
#example args for an export of an counter
python export.py value yourcounter smtp.exaple.com sender-email smpt-server-port recieveremail yoursenderemailpassword
#example args for an export of the simplecount.log file
python export.py log none smtp.exaple.com sender-email smpt-server-port recieveremail yoursenderemailpassword
```
the first arg must be what you want to export log for the log file and value for the value of an counter
the second arg must be the name of your counter or if you want to export your logfile ```none```
the third must be the smtp server of your sender email adress
the fourth arg must be your email adress with you want to send the email from
the fith arg must be the port number of your smtpserver #usually its 465 
the sixt must be the email adress you want the email sent to
the last arg must be your email password