from tkinter import *
from tkinter import messagebox as msg
import pyscreenrec
root=Tk()
root.geometry("400x600")
root.title("VLC Screen Recorder")
root.config(bg="white")
root.resizable(False,False)

recording=pyscreenrec.ScreenRecorder()
icon1=PhotoImage(file="icon.png")
root.iconphoto(False,icon1)

#functions
def start_rec():
    file=filename.get()
    recording.start_recording(str(file+".mp4"),10)# Fps
    msg.showinfo("Screen Recorder v1.0","The recording has started")

def pause_rec():
    recording.pause_recording()
    msg.showinfo("Screen Recorder v1.0","The recording is paused")

def resume_rec():
    recording.resume_recording()
    msg.showinfo("Screen Recorder v1.0","The recording is resumed")

def stop_rec():
    recording.stop_recording()
    msg.showinfo("Screen Recorder v1.0","The recording is complete \n Thanks for using Screen recorder v1.0")


#plotting the images
image1=PhotoImage(file="yellow.png")
Label(root,image=image1,bg="white").place(x=-2,y=40)

image2=PhotoImage(file="blue.png")
Label(root,image=image2,bg="white").place(x=223,y=200)

heading=Label(root,text= "Screen Recorder",bg="white",font=" Kristi 15 bold italic  ")
heading.pack(pady=20)

image3=PhotoImage(file="recording.png")
Label(root,image=image3,bg="white",bd=0).pack(pady=30)

#user input for file_name
filename=StringVar()
entry=Entry(root,textvariable=filename,width=20,font="arial 10")
entry.place(x=100,y=350)
filename.set("Please enter file_Name")


# Buttons 
start_button=Button(root,text="START",bd=0,font="arial 15",bg="black",fg="white",command=start_rec)
start_button.place(x=135,y=255)

# other buttons plotting using images
image4=PhotoImage(file="pause.png")
pausebutton=Button(root,image=image4,bd=0,font="arial 15",bg="white",command=pause_rec)
pausebutton.place(x=50,y=450)


image5=PhotoImage(file="resume.png")
resume_button=Button(root,image=image5,bd=0,font="arial 15",bg="white",command=resume_rec)
resume_button.place(x=150,y=450)


image6=PhotoImage(file="stop.png")
stop_button=Button(root,image=image6,bd=0,font="arial 15",bg="white",command=stop_rec)
stop_button.place(x=250,y=450)




root.mainloop()







# Gaurav4720002