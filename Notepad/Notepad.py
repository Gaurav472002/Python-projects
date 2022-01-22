from tkinter import *
from tkinter.messagebox import showinfo
import os
import re
from tkinter.filedialog import  askopenfilename, asksaveasfilename


def newfile():  # Function to create a new textfile
    global file
    root.title("Untitled- Notepad")
    file = None
    # clears all the text in the textarea from 1st lines 0th character to the end of Textarea
    Textarea.delete(1.0, END)


def openfile():  # Function to open an existing file
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[(
        "All files", "*.*"), ("Text files"".txt")])  # Setting Default extensions for the file

    if file == "":
        file = None
        showinfo("Notepad", "Sorry this file doesnt exists")

    else:
        # Setting the title of the text file by extracting it through directory
        root.title(os.path.basename(file)+"-Notepad")
        Textarea.delete(1.0, END)
        f = open(file, "r")
        Textarea.insert(1.0, f.read())
        f.close()


def savefile():  # Function to save the file
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[
                                 ("All files", "*.*"), ("Text files"".txt")])
        # default file name to save will be untitled.txt
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(Textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file)+"-Notepad")
            showinfo("Notepad V1.47", "File Saved Successfully")
    else:
        f = open(file, "w")
        f.write(Textarea.get(1.0, END))
        f.close()
        showinfo("Notepad", "File Saved Successfully")




def destroyfile():
    root.destroy()  # Function to close the file


def CutText():
    Textarea.event_generate(("<<Cut>>"))  # Function to cut the selected text


def CopyText():
    Textarea.event_generate(("<<Copy>>"))  # Function to copy the selected text


def PasteText():
    # Function to Paste the selected text
    Textarea.event_generate(("<<Paste>>"))


def showabout():
    showinfo("Notepad v1.47",
             " For any queries or help visit www.gaurav_notepad.com")  # Function to display any info for Help

def wordcount(): # function to count the number of words
        words = Textarea.get( '1.0', 'end-1c' )
        wordcount = len( re .findall( '\w+', words ) )
       
        a= wordcount 
        showinfo(f"Notepad v1.47",f"The word count is {a}")
       
        


if __name__ == '__main__':
    root = Tk()
    root.title("Untitled")
    root.geometry("764x600")
    root.wm_iconbitmap("1.ico")  # add icon to your application

    # Creating the text area inside the notepad

    Textarea = Text(root, font="Arial, 15")
    file = None
    Textarea.pack(expand=True, fill=BOTH)

    Menubar = Menu(root)
    # File menu
    Filemenu = Menu(Menubar, tearoff=0)

    Filemenu.add_command(label="New", command=newfile)
    Filemenu.add_command(label="Open", command=openfile)
    Filemenu.add_command(label="Save", command=savefile)
    Filemenu.add_command(label="Exit", command=destroyfile)
    Filemenu.add_command(label="Wordcount", command=wordcount)
 
    Menubar.add_cascade(label="File", menu=Filemenu)

    # Edit menu
    Editmenu = Menu(Menubar, tearoff=0)

    Editmenu.add_command(label="Cut", command=CutText)
    Editmenu.add_command(label="Copy", command=CopyText)
    Editmenu.add_command(label="Paste", command=PasteText)
    Menubar.add_cascade(label="Edit", menu=Editmenu)

    # Help Menu
    Helpmenu = Menu(Menubar, tearoff=0)

    Helpmenu.add_command(label="About", command=showabout)
    Menubar.add_cascade(label="Help", menu=Helpmenu)

    root.config(menu=Menubar)

    # Setting up the scrollbar

    scroll = Scrollbar(Textarea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=Textarea.yview)
    Textarea.config(yscrollcommand=scroll.set)

    # Setting up the statusbar
    statusvar = StringVar()
    statusvar.set(f"Notepad version 1.47")
    sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
   
    sbar.pack(side=BOTTOM, fill=X)

    
       
    root.mainloop()













































   #This simple Notepad is created by Gaurav_472002