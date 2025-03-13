from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os
from stegano import lsb

'''tkinter: The standard GUI toolkit for Python.
filedialog: Module from tkinter used for opening file selection dialogs.
Pillow (PIL): Provides advanced image processing capabilities (used here to load and display images).
os: Used for interacting with the operating system (e.g., accessing files).
stegano.lsb: A steganography library for hiding and revealing data in images using the Least Significant Bit (LSB) technique.'''


root=Tk()
root.title("Steganography-Hide a secret Text Message in an Image")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.configure(bg="#2f4155")

'''Tk(): Creates the root window for the application.
title: Sets the window title.
geometry: Sets the size (700x500) and the position (+150+180) of the window.
resizable: Prevents resizing of the window.
configure: Sets the background color to #2f4155.'''


def showimage():
   global filename
   filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                       title="Select Image File",
                                       filetype=(("PNG file","*.png"),
                                                  ("JPG File",".jpg"),("All file",".txt")))
   img=Image.open(filename)
   img=ImageTk.PhotoImage(img)
   lbl.configure(image=img,width=250,height=250)
   lbl.image=img


'''showimage: Function to open an image file and display it in the GUI.
filedialog.askopenfilename: Opens a dialog for selecting an image file.
initialdir: Starts the file dialog in the current working directory.
filetype: Restricts file types to PNG, JPG, and TXT.
Image.open: Loads the selected image.
ImageTk.PhotoImage: Converts the image to a format suitable for tkinter.
lbl.configure: Updates the label to display the loaded image.'''



def Hide():
    global secret
    message=text1.get(1.0,END)
    secret=lsb.hide(str(filename),message)
'''Hide: Hides a text message in the selected image.
text1.get: Retrieves the text entered in the text box.
lsb.hide: Encodes the message into the image.'''


def Show():
    clear_message=lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)

'''Show: Reveals the hidden message from the image.
lsb.reveal: Extracts the hidden message from the image.
text1.delete: Clears the text box.
text1.insert: Displays the revealed message in the text box.'''


def save():
  secret.save("hidden.png")

 ''' save: Saves the modified image with the hidden message as hidden.png.'''

#icon
image_icon=PhotoImage(file="logo.jpg")
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="logo.png")
Label(root,image=logo,bg="#2f4155").place(x=10,y=0)

Label(root,text="CYBER SCIENCE",bg="#2d4155",fg="white",font="arial 25 bold").place(x=100,y=20)

'''iconphoto: Sets a window icon.
logo: Displays a logo at the top left.
Label: Adds text with "CYBER SCIENCE" styled and positioned.'''


#first frame
f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

lbl=Label(f,bg="balck")
lbl.place(x=40,y=10)

'''Frame f: Creates a black-bordered frame for displaying images.
Label lbl: Placeholder for the loaded image.'''


#second frame
frame2=Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
frame2.place(x=350,y=80)


text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


'''Frame frame2: Holds the text box for entering/revealing the message.
Text: Multi-line text box for user input.
Scrollbar: Adds a scrollbar linked to the text box.'''



#third frame
frame3=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)

Button(frame3,text="Open Image",width=10,height=2,font="arial 14 bold",command=showimage).place(x=20,y=30)
Button(frame3,text="Save Image",width=10,height=2,font="arial 14 bold",command=save).place(x=180,y=30)
Label(frame3,text="Picture,Image,Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)

'''Frame frame3: Buttons for opening and saving images.
Buttons: Call respective functions (showimage and save).'''



#fourth frame
frame4=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4,text="Hide Data",width=10,height=2,font="arial 14 bold",command=Hide).place(x=20,y=30)
Button(frame4,text="Show Data",width=10,height=2,font="arial 14 bold",command=Show).place(x=180,y=30)
Label(frame4,text="Picture,Image,Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)

'''Frame frame4: Buttons for hiding and revealing data.
Buttons: Call respective functions (Hide and Show).'''




root.mainloop()

'''mainloop: Keeps the GUI running, waiting for user interaction.'''
