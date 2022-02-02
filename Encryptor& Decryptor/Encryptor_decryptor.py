
from tkinter import *
from tkinter import messagebox

import base64



# Function to encrypt the text
def encrypt():
    password=code.get()

    if password=="472002":
        screentop=Toplevel(screen)
        screentop.title("Encryption")
        screentop.geometry("500x200")
        screentop.config(bg="red")
        screentop.resizable(False,False)

        message=text1.get(1.0,END)
        encoded_message=message.encode("ascii")
        base64_b=base64.b64encode(encoded_message)
        encrypt=base64_b.decode("ascii")

        Label(screentop,text="ENCRYPT..",fg="white",font="arial 12  ",bg="red").place(x=10,y=0)

        text2=Text(screentop,font=" arial 12",bg="white",relief=GROOVE,bd=0,wrap=WORD)
        text2.place(x=10,y=50,width=555,height=100)
        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("Encryption","Please Input password")
    elif password !="472002":
        messagebox.showerror("Encryption","Invalid! password")

# Function to decrypt the text
def decrypt():
    password=code.get()

    if password=="472002":
        screentop1=Toplevel(screen)
        screentop1.title("Decryption")
        screentop1.geometry("500x200")
        screentop1.config(bg="green")
        screentop1.resizable(False,False)

        message=text1.get(1.0,END)
        encoded_message=message.encode("ascii")
        base64_b=base64.b64decode(encoded_message)
        decrypt=base64_b.decode("ascii")

        Label(screentop1,text="DECRYPT..",fg="white",font="arial 12  ",bg="green").place(x=10,y=0)

        text2=Text(screentop1,font=" arial 12",bg="white",relief=GROOVE,bd=0,wrap=WORD)
        text2.place(x=10,y=50,width=555,height=100)
        text2.insert(END,decrypt)

    elif password=="":
        messagebox.showerror("Decryption","Please Input password")
    elif password !="472002":
        messagebox.showerror("Decryption","Invalid! password")
    

def reset():
    code.set("")
    text1.delete(1.0,END)

def mainfunc():
    global screen
    global code
    global text1
    
    screen=Tk()
    screen.geometry("580x400")
    screen.title("Encrypter- Decrypter")
    # icon=PhotoImage(file="icon1.png")
    # screen.iconphoto(False,icon)
    screen.iconbitmap(r"E:\\Programming---Codes\\Python Projects\\Encryptor& Decryptor\\icon1.ico")
    screen.config(bg="purple")

    Label(text="Enter the text for encryption and decryption",fg="black",font="arial 12 bold underline italic ").place(x=10,y=10)
    text1=Text(font=" arial 15",bg="white", borderwidth=5,relief=SUNKEN,wrap=WORD)
    text1.place(x=10,y=50,width=555,height=100)

    Label(text="Enter the Password",fg="black",font="arial 12 bold underline italic ").place(x=10,y=160)
    code=StringVar()
    Entry( textvariable=code,font=("arial",15), borderwidth=5,show="*",bg="white",relief=SUNKEN).place(x=280,y=160,width=200,height=30)

    encrypt_button=Button(screen,width=8,height=1,borderwidth=10,relief=SUNKEN,fg="white",
    bg="red",text=" ENCRYPT", font=" Arial 12 bold italic",command=encrypt).place(x=30,y=230)


    decrypt_button=Button(screen,width=8,height=1,borderwidth=10,relief=SUNKEN,fg="white",
    bg="green",text="DECRYPT", font=" Arial 12 bold italic",command=decrypt).place(x=400,y=230)

    reset_button=Button(screen,width=8,height=1,borderwidth=10,relief=SUNKEN,fg="white",
    bg="blue",text=" RESET", font=" Arial 12 bold italic",command=reset).place(x=200,y=300)

    screen.mainloop()


mainfunc()