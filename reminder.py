from plyer import notification     #The package which contains the notify method
import datetime   #Notifies every hour
from time import sleep
import getpass
import os
# from tkinter import *
# All the global variables are here
reminders = []#holds the minutes of interval between two reminders. 0th index
# holds for water 1st for eyes and 2nd holds for body
USER_NAME = getpass.getuser()
times = []#holds the times in mnutes at which the reminders are to be sent.

# __________________________________________
# All the methods start from here

def next_reminder(time_now):
    for i in reminders:
        if time_now+i>=60:
            times.append(time_now+i - 60)
        else:
            times.append(time_now+i)


def added_to_startup():
    with open("reminderappfile1.txt","w+") as file:
        if file.read() == "":
            file.write("True")
            return False
        else:
            return True

def are_reminders_set():
    with open("reminderapp_file2.txt","a+") as file:
        lines = file.readlines()
        if lines == []: return False
        else:
            for i in lines:
                if "\n" in i:
                    i.replace("\n","")
                i = int(i)
            global reminders
            reminders = lines
            return True

# def gui():
#     frame = Tk()
#
#
#     frame.mainloop()

#Function which sends a notification after taking input(as a string) the notification to send
def send_notification(notificate,message):
    notification.notify(title=notificate,
                        message = message,
                        timeout = 50)

def send_notification_multiple(notificate,notificate2):
    notification.notify(title = notificate+" & "+notificate2,
                        timeout = 50)

#Checks if it is time to send the notification, if it is, it does
def is_time():
    if datetime.datetime.now().strftime("%M") in times:
        return True
    else:
        return False


#The following code runs the program automatically on startup



def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "reminder.bat", "w+") as bat_file:
        bat_file.write(r'start %s' % file_path)
    with open("reminderappfile1.txt","w+") as file:
        file.write("True")



def set_reminders():
    global reminders
    reminders = [
        int(input("How many minutes of interval do you want between \"drink water\" reminders?\n")),
        int(input("How many minutes of interval do you want between \"exercise eyes\" reminders?\n")),
        int(input("How many minutes of interval do you want between \"move around\" reminders?\n"))]
    with open("reminderapp_file2.txt","w+") as file:
        file.write(str(reminders[0]) +"\n" + str(reminders[1]) + "\n" + str(reminders[2]))


# ______________________________________________________________
# The main process i.e, the logic
if added_to_startup() == False:
    if input("Do you want the app to start everytime you open the computer?y/n")=="y":
        add_to_startup("")
if are_reminders_set() == False:
    set_reminders()
while True:
    if datetime.datetime.now().strftime("%S") == "00":
        next_reminder(int(datetime.datetime.now().strftime("%M")))
        reminders_sent=0
        while reminders_sent is not 3:
            if is_time()==True:
                #The following is the entire process of sending the reminder
                index = times.index(int(datetime.datetime.now().strftime("%M")))
                remind = ""
                message = ""
                if index == 0:
                    remind = "Drink water"
                    message = "Go drink a glass of water"
                elif index == 1:
                    remind = "Rest your eyes now"
                    message = "Exercise your eyes or rest them"
                else:
                    remind = "Move around"
                    message = "Go move around"
                send_notification(remind,message)
                reminders_sent+=1
            else:
                sleep(60)




