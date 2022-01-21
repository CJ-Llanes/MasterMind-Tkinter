
from tkinter import *
# Importing tkPDFViewer to place pdf file in gui. 
from tkPDFViewer import tkPDFViewer as pdf 
def languageWindow(window, state):
    newWindow = Toplevel(window)
    newWindow.title("How to Play...")
    newWindow.geometry("670x500")
    if state==True:
        vEnglish = pdf.ShowPdf() 
        vEnglishOpen = vEnglish.pdf_view(newWindow, 
                    pdf_location = r"MasterEnglish.pdf",  
                    width = 670, height = 500)
        vEnglishOpen.pack()
    else:
        vSpanish = pdf.ShowPdf() 
        vSpanishOpen = vSpanish.pdf_view(newWindow, 
                    pdf_location = r"MasterSpanish.pdf",  
                    width = 670, height = 500)
        vSpanishOpen.pack()



    