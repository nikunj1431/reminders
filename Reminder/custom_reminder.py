import datetime
from plyer import notification

hour = ""
minute = ""
message = ""
title = ""
day = ""
month = ""
other_day = False

def set_reminder():#This method inputs all the details needed for the reminder.

    if input("Do you want the reminder for today or any other day?(t/o)") == "o":
        global day,month,other_day
        month = input("Which month do you want the reminder for(1 for January, 12 for december)")
        day = input("What date do you want the reminder for?")
        other_day = True
    print("At what time do you want to set the reminder for?")
    global hour, minute,message,title
    hour = input("Enter the hour in 24 hour format")
    minute = input("Enter the minute")
    title = input("About what do you want the notification to be?")
    message = input("What message do you want in your notification?")


def is_time_custom():#checks if it is time yet to send the notification
    if other_day == True:
        if datetime.datetime.now().strftime("%d") == day and datetime.datetime.now().strftime("%m") == month:
            pass#If it is the day to send the reminder, it will continue
        else:
            return False# If not, it will immediateky returen False
    # The following checks if the it is the day to send the reminder
    time_now = datetime.datetime.now()
    if time_now.strftime("%H") == hour and time_now.strftime("%M") == minute:
        return True
    else:
        return False

def send_notification():#sends the notification
    notification.notify(title = title,
                        message = message,
                        timeout = 30,
                        app_icon = "reminder.ico")