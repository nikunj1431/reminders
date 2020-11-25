from tkinter import *
from PIL import Image
from tkinter import ttk

root = Tk()
root.title("Reminder")

# The following block of code adds an image to the title.
img_png = Image.open("icons\\reminder_window_img.jpg")
img_png.save("reminder_window_img.png","PNG")
img = PhotoImage(file = "reminder_window_img.png")
root.iconphoto(True,img)

# The following block of code sets the icon image for the window


#The following code sets all that needs to appear on the screen

minute_text = StringVar()
minute_dropdown = ttk.Combobox(root, width = 30, textvariable = minute_text)
minute_dropdown["values"] = ("1" , "2" , "3", "4", "5", "6", "7" , "8" ,"9" , "10", "11", "12" ,"13", "14" , "15", "16", "17" ,"18" ,"19" , '20' ,'21', '22' , '23' ,'24' , '25' , '26' , '27' , '28' , '29' , '30' , '31' , '32', '33','34' ,'35', '36' , '37', '38', '39', '40' ,'41' ,'42' ,'43' , '44', '45' , '46', '47','48', '49', '50' ,'51' , '52', '53', '54', '55', '56' ,'57', '58' , '59', '60')
minute_dropdown.current(44)
minute_dropdown.pack()
#Function to be called when button is pressed
def submit():
    global minute
    minute = int(minute_text.get())
button_submit = Button(root , command = submit, text = "OK")
button_submit.pack()

#The following block of code sets teh geometry for the window
root.geometry("500x500")
root.minsize(500,500)
root.maxsize(500,500)

label_title = Label(root, text = "Reminder")
label_title.pack()



root.mainloop()