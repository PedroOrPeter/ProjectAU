import os


# Start SMTP Local Server
def start_server():
    os.system("start /wait cmd /c {python -m smtpd -c DebuggingServer -n localhost:1025}")
