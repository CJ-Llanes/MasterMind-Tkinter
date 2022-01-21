from tkinter import *
# Importing tkPDFViewer to place pdf file in gui. 
from tkPDFViewer import tkPDFViewer as pdf 
import numpy
import random
import instructions


def main():
    # Set Size and position of the window
    height, width, xoffset, yoffset = 670, 450, 400, 20
    window = Tk()
    window.geometry("%dx%d%+d%+d" % (width, height, xoffset, yoffset))

    window.title("MasterMind")

    # Presentation text
    introText="Welcome to MasterMind!!!\n Let's gonna play Folk!!"
    lbl = Label(window, text=introText,font=("Ubuntu Condensed", 13, "italic"))
    lbl.place(x=int(width*1/4), y=20)
    lbl2 = Label(window, text="Rules"
    ,font=("Ubuntu Condensed", 12, "italic"))
    lbl2.place(x=int(width*2/4)-55, y=height/2-90)

    # Set buttons and Position
    englishButton = Button(window, text="English",height=1,width=6, 
    command = instructions.languageWindow(window,True))
    englishButton.place(x=int(width*1/4), y=height/2-50)

    spanishButton = Button(window, text="Spanish",height=1,width=6,
    command = instructions.languageWindow(window,False))
    spanishButton.place(x=int(width*2/4), y=height/2-50)


    #Configure the row/col of our frame and root window to be resizable and fill all available space


    
    window.mainloop()

main()