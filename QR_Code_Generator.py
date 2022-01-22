from tkinter import *
import qrcode
root=Tk()

root.geometry("1000x550")
root.title("QR Code Generator")
root.config(bg="purple")
root.resizable(False,False)



def generate():
    name=title.get() 
    text=entry.get()
    qr=qrcode.make(text)
    qr.save("QR_Code/"+str(name)+".png")
    
    global Image
    Image=PhotoImage(file="QR_Code/"+str(name)+".png")
    Image_Display.config(image=Image)

Image_Display=Label(root,bg="purple")
Image_Display.pack(padx=50,pady=10,side=RIGHT)

# adding icon in the gui
icon1=PhotoImage(file="QRicon.png")
root.iconphoto(False,icon1)

Label(root,text="Title For QR",fg="white",bg="purple",font="Arial 20 italic bold underline").place(x=40,y=130)

title=Entry(root,width=15,font="Arial 15") 
title.place(x=40,y=190)

Label(root,text="Enter the Website url",fg="white",bg="purple",font="Arial 20 italic bold underline").place(x=40,y=280)

entry=Entry(root,width=25,font="Arial 15") 
entry.place(x=40,y=340)
Button(root,text="GENERATE",width=20,height=2,bg="black",fg="white",font="Arial 12 bold",borderwidth=5,relief=SUNKEN,command=generate ).place(x=50, y=400)

root.mainloop()