from msilib.schema import Font
from tkinter import *
import os
from unittest import skipUnless

def shutdown():
    os.system("shutdown /s /t 1")

def restart():
    os.system("shutdown /r /t 1")

def logout():
    os.system(("shutdown -1"))


root=Tk()
root.title(" SHUT DOWN APP")
root.geometry("600x500")
root.config(bg="purple")
root.resizable(False,False)
icon1=PhotoImage(file="shut.png")
root.iconphoto(False,icon1)


power_button=Button(root,width=10,height=2,borderwidth=10,relief=SUNKEN,fg="white",
bg="black",text=" POWER", font=" Arial 15 bold italic",command=shutdown).place(x=40,y=100)


restart_button=Button(root,width=10,height=2,borderwidth=10,relief=SUNKEN,fg="white",
bg="black",text=" RESTART", font=" Arial 15 bold italic",command=restart).place(x=330,y=100)

logout_button=Button(root,width=10,height=2,borderwidth=10,relief=SUNKEN,fg="white",
bg="black",text=" LOGOUT", font=" Arial 15 bold italic",command=logout).place(x=180,y=250)
root.mainloop()








#Gaurav472002