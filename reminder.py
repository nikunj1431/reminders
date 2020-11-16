from plyer import notification
import datetime
from time import sleep

interval = int(input("After how many minutes do want a reminder?"))
last_reminder_sent = int(datetime.datetime.now().strftime("%M"))

def is_time(time):
    if last_reminder_sent + interval == time:
        return True
    elif (last_reminder_sent + interval) - 60 == time:
        return True
    else:
        return False

while True:
    if datetime.datetime.now().strftime("%S") == "00":
        if is_time(int(datetime.datetime.now().strftime("%M"))) == True:
            notification.notify(title = "Take a break",
                                message = "Take a break, rest your eyes, move around and drink water",
                                timeout = 30,
                                app_icon = "D:\\Downloads\\remindericon.ico")
            last_reminder_sent = int(datetime.datetime.now().strftime("%M"))
        else:
            sleep(60)
