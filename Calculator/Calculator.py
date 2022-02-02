from tkinter import *
from tkinter.messagebox import showinfo

root= Tk()
root.geometry("570x620")
root.title("Calculator v1.0")
root.resizable(False,False)
root.config(bg="black")
root.wm_iconbitmap(r"E:\\Programming---Codes\\Python Projects\\Calculator\\2.ico")

equation = ""

result_screen=Label(root,width=55,height=3,text="",font="Arial,30",borderwidth=8,relief=SUNKEN) # Creating the result screen of the calculator
result_screen.pack()


def show(value):
    global equation
    equation+=value
    result_screen.config(text=equation) # Function to show the values on the screen after clicking



def clear():
    global equation
    equation=""
    result_screen.config(text=equation) #Function to clear the screen

def calculate():
    global equation
    result=""
    if equation !="":   # FUnction to evaluate the various operations in the calculator
        try:
            result=eval(equation)
        except:
            result="Error!"
            equation=""
    result_screen.config(text=result)

def showabout():
    showinfo("Calculator v1.47",
             "  This Calculator is created by Gaurav \nFor any queries or help visit www.gaurav_Codes.com")

# Creating Buttons for the calculator..            

Button(root,text="C",width=10,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#3697f5",command=lambda:clear()).place(x=10,y=100)
Button(root,text="/",width=10,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#2a2d36",command=lambda:show("/")).place(x=150,y=100)
Button(root,text="*",width=10,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#2a2d36",command=lambda:show("*")).place(x=290,y=100)
Button(root,text="%",width=10,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#2a2d36",command=lambda:show("%")).place(x=430,y=100)

Button(root,text="7",width=10,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#2a2d36",command=lambda:show("7")).place(x=10,y=200)
Button(root,text="8",width=10,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#2a2d36",command=lambda:show("8")).place(x=150,y=200)
Button(root,text="9",width=10,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#2a2d36",command=lambda:show("9")).place(x=290,y=200)
Button(root,text="+",width=10,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#2a2d36",command=lambda:show("+")).place(x=430,y=200)

Button(root,text="4",width=10,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#2a2d36",command=lambda:show("4")).place(x=10,y=300)
Button(root,text="5",width=10,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#2a2d36",command=lambda:show("5")).place(x=150,y=300)
Button(root,text="6",width=10,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#2a2d36",command=lambda:show("6")).place(x=290,y=300)
Button(root,text="-",width=10,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#2a2d36",command=lambda:show("-")).place(x=430,y=300)

Button(root,text="3",width=10,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#2a2d36",command=lambda:show("3")).place(x=10,y=400)
Button(root,text="2",width=10,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#2a2d36",command=lambda:show("2")).place(x=150,y=400)
Button(root,text="1",width=10,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#2a2d36",command=lambda:show("1")).place(x=290,y=400)
Button(root,text="0",width=22,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#2a2d36",command=lambda:show("0")).place(x=10,y=500)

Button(root,text=".",width=10,height=3,font="Arial,30,Bold",bd=3,relief=SUNKEN,fg="white",bg="#2a2d36",command=lambda:show(".")).place(x=290,y=500)
Button(root,text="=",width=10,height=7,font="Arial,1000,Bold",bd=3,relief=SUNKEN,fg="white",bg="orange",command=lambda:calculate()).place(x=430,y=400)

mymenu=Menu(root)
mymenu.add_command(label="About",command=showabout)
root.config(menu=mymenu)  # Adding about menu on the top of the calculator

root.mainloop()



































# Gaurav4720002...:)