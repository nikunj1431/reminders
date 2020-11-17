from plyer import notification
import datetime
from time import sleep
import custom_reminder



def is_time():
    current_time = int(datetime.datetime.now().strftime("%M"))
    if last_reminder_sent + interval == current_time:
        return True
    elif (last_reminder_sent + interval) - 60 == current_time:
        return True
    else:
        return False

if input("Do you want a reminder at a fixed time?(y/n)") == "y":
    custom_reminder.set_reminder()
interval = int(input("After how many minutes do want a reminder?"))
last_reminder_sent = int(datetime.datetime.now().strftime("%M"))
while True:
    if datetime.datetime.now().strftime("%S") == "00":
        if custom_reminder.is_time() == True:
            custom_reminder.send_notification()
        if is_time() == True:
            notification.notify(title = "Take a break",
                                message = "Take a break, rest your eyes, move around and drink water",
                                timeout = 30,
                                app_icon = "D:\\Downloads\\remindericon.ico")
            last_reminder_sent = int(datetime.datetime.now().strftime("%M"))
        else:
            sleep(60)
