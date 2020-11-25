from tkinter import *
from PIL import Image
from tkinter import ttk
from time import sleep

root = Tk()
root.title("Reminder")
label_title = Label(root, text = "Reminder")
label_title.pack()

# The following block of code adds an image to the title.
img_png = Image.open("icons\\reminder_window_img.jpg")
img_png.save("reminder_window_img.png","PNG")
img = PhotoImage(file = "reminder_window_img.png")
root.iconphoto(True,img)

# The following block of code sets the icon image for the window


#The following code sets all that needs to appear on the screen
#Dropdown for interval
Label(root, text = "After how many minutes do you want a reminder?").pack()
minute_text = StringVar()
minute_dropdown = ttk.Combobox(root, width = 30, textvariable = minute_text)
minute_dropdown["values"] = ("1" , "2" , "3", "4", "5", "6", "7" , "8" ,"9" , "10", "11", "12" ,"13", "14" , "15", "16", "17" ,"18" ,"19" , '20' ,'21', '22' , '23' ,'24' , '25' , '26' , '27' , '28' , '29' , '30' , '31' , '32', '33','34' ,'35', '36' , '37', '38', '39', '40' ,'41' ,'42' ,'43' , '44', '45' , '46', '47','48', '49', '50' ,'51' , '52', '53', '54', '55', '56' ,'57', '58' , '59', '60')
minute_dropdown.current(44)
minute_dropdown.pack()

#The checkbox for asking if the user wants the app to be added to startup
Label(root, text = "Do you want the app to start every time you start your device? If you have already turned it on, no need to do it again.").pack()
add_to_startup = IntVar()
add_to_startup_check = Checkbutton(root, variable = add_to_startup)
add_to_startup_check.pack()

#Function to be called when button is pressed

button_submit = Button(root , command = submit, text = "OK")
button_submit.pack()

#The following block of code sets teh geometry for the window
root.geometry("500x500")
root.minsize(500,500)
root.maxsize(500,500)


def submit():
    global minute,add_to_startup
    minute = int(minute_text.get())
    add_to_startup = bool(int(add_to_startup.get()))
    return minute,add_to_startup

def close_app_for_startup():
    window = Tk()
    Label(window, text = "Please restart the app. The app will close automatically after 10 seconds").pack()
    sleep(10)
    global root
    root.destroy()
    window.destroy()
    exit(0)

root.mainloop()