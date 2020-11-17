import datetime
from plyer import notification

hour = ""
minute = ""
message = ""
title = ""
timeout = 30

def set_reminder():
    print("At what time do you want to set the reminder for?")
    global hour, minute,message,title, timeout
    hour = input("Enter the hour in 24 hour format")
    minute = input("Enter the minute")
    title = input("About what do you want the notification to be?")
    message = input("What message do you want in your notification?")
    timeout = int(input("(Optional) After how many seconds should the notification dissapear")

def is_time():
    time_now = datetime.datetime.now()
    if time_now.strftime("%H") == hour and time_now.strftime("%M") == minute:
        return True
    else:
        return False

def send_notification():
    notification.notify(title = title,
                        message = message,
                        timeout = timeout,
                        app_icon = r"D:\Downloads\reminder.ico")