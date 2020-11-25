from plyer import notification
import datetime
from time import sleep
import custom_reminder
import getpass
import os
import reminder_gui

def add_to_startup():
    if os.path.exists(r"C:\ProgramData\216c40503e"):
        with open(r"C:\ProgramData\216c40503e\reminder.bat","w") as file:
            file_dir = os.path.dirname(os.path.realpath(__file__))
            file_name = "\\reminder.exe"
            file_location = file_dir + file_name
            file.write("Start %s "%file_location)
    else:
        with open(r"C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\reminder.bat", "w") as file:
            file_dir = os.path.dirname(os.path.realpath(__file__))
            file_name = "\\reminder.exe"
            file_location = file_dir + file_name
            file.write("Start %s " % file_location)

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
interval,add_to_startup_var = reminder_gui.submit()

if (os.path.exists(r"C:\ProgramData\216c40503e\reminder.bat") == False or os.path.exists(r"C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\reminder.bat") == False) and add_to_startup_var == True :
    add_to_startup()
    reminder_gui.close_app_for_startup()
    exit(0)


while True:
    if datetime.datetime.now().strftime("%S") == "00":
        if custom_reminder.is_time_custom() == True:
            custom_reminder.send_notification()
        if is_time() == True:
            notification.notify(title = "Take a break",
                                message = "Take a break, rest your eyes, move around and drink water",
                                timeout = 30,
                                app_icon = "icons\\remindericon.ico")
            last_reminder_sent = int(datetime.datetime.now().strftime("%M"))
        else:
            sleep(60)

