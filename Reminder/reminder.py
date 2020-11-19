from plyer import notification
import datetime
from time import sleep
import custom_reminder
import getpass
import os

def add_to_startup():
    with open(r"C:\ProgramData\216c40503e\reminder.bat","w") as file:
        file.write("Start \"\" %s "%__file__)

last_reminder_sent = int(datetime.datetime.now().strftime("%M"))
def is_time():#checks if it is time yet for the notification to be sent
    current_time = int(datetime.datetime.now().strftime("%M"))
    if last_reminder_sent + interval == current_time:
        return True
    elif (last_reminder_sent + interval) - 60 == current_time:
        return True
    else:
        return False

# The following is the main logic of the program.
if input("Do you want a reminder at a fixed time?(y/n)") == "y":
    custom_reminder.set_reminder()


if input("Do you want the program to start every time you start the computer?(y/n)") == "y" and os.path.exists("C:\ProgramData\216c40503e\reminder.bat") == False:
    print("Please start the program again")
    sleep(10)
    add_to_startup()
    exit(0)

interval = int(input("After how many minutes do want a reminder?"))
while True:
    if datetime.datetime.now().strftime("%S") == "00":
        if custom_reminder.is_time_custom() == True:
            custom_reminder.send_notification()
        if is_time() == True:
            notification.notify(title = "Take a break",
                                message = "Take a break, rest your eyes, move around and drink water",
                                timeout = 30,
                                app_icon = "remindericon.ico")
            last_reminder_sent = int(datetime.datetime.now().strftime("%M"))
        else:
            sleep(60)
