

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from unicodedata import name
import pytz
import requests
from geopy.geocoders import Nominatim 
from timezonefinder import TimezoneFinder
from datetime import date, datetime


root=Tk()
root.geometry("900x500+500+200")
root.title("Weather app v1.0")
# icon1=PhotoImage(file="sunlogo.png")
# root.iconphoto(False,icon1)
root.iconbitmap(r"E:\\Programming---Codes\\Python Projects\\Weather-App\\sunlogo.ico")
# FUnction to get the weather details

def Get_weather():
    try:
        city=textarea.get()
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I: %M %p")
        clock.config(text=current_time)
        current.config(text="CURRENT WEATHER")

        # Extracting wather data using API

        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=260a21f28d30c58471bebbe7e84dbe26"
        
        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception:
        messagebox.showerror("Weather App v1.0","Invalid Entry!!")
   




# GUI of the app

search_image=PhotoImage(file="E:\\Programming---Codes\\Python Projects\\Weather-App\\search.png")
image1=Label(image=search_image)
image1.place(x=20,y=20)

textarea=tk.Entry(root,justify="center",width =17,font=" poppins 15 bold",bg="#404040",fg="white",bd=0)
textarea.place(x=50,y=40)
textarea.focus()


search_icon=PhotoImage(file="E:\\Programming---Codes\\Python Projects\\Weather-App\\search_icon.png")
image2=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=Get_weather)
image2.place(x=400,y=34)

logo=PhotoImage(file="E:\\Programming---Codes\\Python Projects\\Weather-App\\logo.png")
image3=Label(image=logo)
image3.place(x=150,y=120)


bottom_box=PhotoImage(file="E:\\Programming---Codes\\Python Projects\\Weather-App\\box.png")
image4=Label(image=bottom_box)
image4.pack(padx=5,pady=5,side=BOTTOM)

# adding labels 
label1=Label(root,text="WIND",font="Helvetica 15 bold",fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font="Helvetica 15 bold",fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font="Helvetica 15 bold",fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font="Helvetica 15 bold",fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

#Desc label
current=Label(root,font="arial 15 bold")
current.place(x=30,y=100)

# clock label
clock=Label(root,font=" Helventica 20 bold")
clock.place(x=30,y=130)

t=Label(font="arial 70 bold",fg="#ee6668")
t.place(x=400,y=150)

c=Label(font="arial 15 bold")
c.place(x=400,y=280)

w=Label(text="...",font="arial 20 bold",bg="#1ab5ef")
w.place(x=120,y=430)

h=Label(text="...",font="arial 20 bold",bg="#1ab5ef")
h.place(x=280,y=430)

d=Label(text="...",font="arial 20 bold",bg="#1ab5ef")
d.place(x=450,y=430)

p=Label(text="...",font="arial 20 bold",bg="#1ab5ef")
p.place(x=670,y=430)

root.mainloop()






