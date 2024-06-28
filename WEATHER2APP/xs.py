from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import mysql.connector as mycon

root=Tk()
root.title("WEATHER APP")
root.geometry("900x500")
root.configure(bg="#57adff")
root.resizable(False,False)


def getweather():
    city = textf.get()

    getloc = Nominatim(user_agent="geopiExercise")
    location = getloc.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    home = pytz.timezone(result)
    localt = datetime.now(home)
    current_t = localt.strftime("%I:%M:%p")
    clock.config(text=current_t)
    current_d = localt.strftime("%d-%m-%Y")
    date1.config(text=current_d)
    long1.config(text=f"{round(location.latitude, 4)}°N,{round(location.longitude, 4)}°E")
    name.config(text="CURRENT WEATHER")

    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=1be6666b3f28e54c35779e4ca6a28f42"

    json_d = requests.get(api).json()
    con1 = json_d['weather'][0]['main']
    des = json_d['weather'][0]['description']
    temp = int(json_d['main']['temp'] - 273.15)
    pre = json_d['main']['pressure']
    hum = json_d['main']['humidity']
    wind = json_d['wind']['speed']

    con = mycon.connect(host='127.0.0.1', user='root', password="root")
    cur = con.cursor()
    cur.execute("create database if not exists weather")
    cur.execute("use weather")
    cur.execute("create table if not exists Data( D_S_name Varchar(70), temp float,wind_speed float, pressure float, humidity float, description varchar(30),Predictions varchar(150))")
    con.commit()
    query = "insert into Data values('{}',{},{},{},{},'{}','{}')".format(city, temp, wind, pre, hum, des, con1)
    cur.execute(query)
    con.commit()
    print("## Data Saved ##")

    t.config(text=(temp, "°"))
    c.config(text=(con1, "|", "FEELS", "LIKE", temp, "°"))
    w.config(text=(wind, "m/s"))
    h.config(text=(hum, "%"))
    d.config(text=des)
    p.config(text=(pre, "hPa"))




image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)


si=PhotoImage(file="Untitled.png")
myimage=Label(image=si,bg="#57adff")
myimage.place(x=20,y=20)

textf=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#131414",border=0,fg="white")
textf.place(x=50,y=40)
textf.focus()

sicon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=sicon,borderwidth=0,cursor="hand2",bg="#131414",command=getweather)
myimage_icon.place(x=400,y=34)

logoi=PhotoImage(file="logo.png")
logo=Label(image=logoi,bg="#57adff")
logo.place(x=200,y=100)


fi=PhotoImage(file="box.png")
fmi=Label(image=fi,bg="#57adff")
fmi.pack(padx=5,pady=5,side=BOTTOM)

name=Label(root,font=("arial",15,"bold "),bg="#57adff")
name.place(x=20,y=100)
date1=Label(root,font=("Helvatica",20),bg="#57adff")
date1.place(x=30,y=125)
clock=Label(root,font=("Helvatica",15),bg="#57adff")
clock.place(x=50,y=155)

l1=Label(root,text="WIND SPEED",font=("Helvetica",15,"bold"),fg="white",bg="#10F3FF")
l1.place(x=115,y=400)

l2=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="white",bg="#10F3FF")
l2.place(x=275,y=400)

l3=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white",bg="#10F3FF")
l3.place(x=430,y=400)

l4=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="white",bg="#10F3FF")
l4.place(x=645,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d",bg="#57adff")
t.place(x=480,y=150)
c=Label(font=("arial",15,"bold"),bg="#57adff")
c.place(x=450,y=250)

w=Label(text="...",font=("arial",15,"bold"),bg="#10F3FF")
w.place(x=125,y=430)

h=Label(text="...",font=("arial",15,"bold"),bg="#10F3FF")
h.place(x=285,y=430)

d=Label(text="...",font=("arial",15,"bold"),bg="#10F3FF")
d.place(x=435,y=430)

p=Label(text="...",font=("arial",15,"bold"),bg="#10F3FF")
p.place(x=675,y=430)

timezone=Label(root,font=("Helvetica",20),fg="white",bg="#57adff")
timezone.place(x=720,y=10)

long1=Label(root,font=("Helvetica",10),fg="white",bg="#57adff")
long1.place(x=730,y=40)


root.mainloop()