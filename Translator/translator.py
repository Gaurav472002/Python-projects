

from tkinter import *
from tkinter import ttk,messagebox as msg
import googletrans
from googletrans import *




root=Tk()
root.geometry("1080x400")
root.title("Translator v1.0")
root.config(bg="white")
root.resizable(False,False)

# function to change the input language given by the user
def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1_text.configure(text=c)
    label2_text.configure(text=c1)

    root.after(1000,label_change)


#function to tanslate the text
def translate_text():
    realtext=text1.get(1.0,END)
    t1=Translator()
    transtext=t1.translate(realtext,src=combo1.get(),dest=combo2.get())
    transtext=transtext.text
    text2.delete(1.0,END)
    text2.insert(END,transtext)
    msg.showinfo("Translator v1.0","Your text has been \n successfully translated")
 

icon1=PhotoImage(file="google.png")
root.iconphoto(False,icon1)

arrow=PhotoImage(file="arrow.png")
image_Label=Label(root,image=arrow,bg="white",width=150)
image_Label.place(x=460,y=50)


language=googletrans.LANGUAGES
all_languages=list(language.values())
lang1=language.keys()

#creating the first combobox

combo1=ttk.Combobox(root,values=all_languages,font="arial 12",state="r")
combo1.place(x=110,y=20)
combo1.set("ENGLISH")

label1_text=Label(root,text="ENGLISH",font="arial 20 bold",bg="white",width=15,bd=5,relief=GROOVE)
label1_text.place(x=70,y=50)

combo2=ttk.Combobox(root,values=all_languages,font="arial 12",state="r")
combo2.place(x=720,y=20)
combo2.set("SELECT ANY")

label2_text=Label(root,text="ENGLISH",font="arial 20 bold",bg="white",width=15,bd=5,relief=GROOVE)
label2_text.place(x=680,y=50)


#creating frame
f=Frame(root,bg="black",bd=5)
f.place(x=10,y=120,width=440,height=210)

text1=Text(f,font="arial 15",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)



f1=Frame(root,bg="black",bd=5)
f1.place(x=630,y=120,width=440,height=210)

text2=Text(f1,font="arial 15",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill='y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# translate Buttton
translate_button=Button(root,text="TRANSLATE",font="arial 15 italic",activebackground="white",cursor="hand2",
bd=5,width=10,height=1,bg="black",fg="white",command=translate_text)
translate_button.place(x=460,y=200)

label_change()

root.mainloop()







#Gaurav 472002