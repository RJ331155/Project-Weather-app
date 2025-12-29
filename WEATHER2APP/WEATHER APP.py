from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import mysql.connector as mycon
import os
from dotenv import load_dotenv

root=Tk()
root.title("WEATHER APP")
root.geometry("900x500")
root.configure(bg="#57adff")
root.resizable(False,False)

def exit_application():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()

def getweather():
   try:
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
       current_d= localt.strftime("%d-%m-%Y")
       date1.config(text=current_d)
       long1.config(text=f"{round(location.latitude, 4)}°N,{round(location.longitude, 4)}°E")
       name.config(text="CURRENT WEATHER")

       load_dotenv()
       api_key = os.getenv("WEATHER_API_KEY")
       api = "https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid="+ api_key

       json_d = requests.get(api).json()
       con = json_d['weather'][0]['main']
       des = json_d['weather'][0]['description']
       temp = int(json_d['main']['temp'] - 273.15)
       pre = json_d['main']['pressure']
       hum = json_d['main']['humidity']
       wind = json_d['wind']['speed']

       t.config(text=(temp, "°"))
       c.config(text=(con, "|", "FEELS", "LIKE", temp, "°"))
       w.config(text=(wind,"m/s"))
       h.config(text=(hum,"%"))
       d.config(text=des)
       p.config(text=(pre,"hPa"))


   except Exception as e:
       city = textf.get()
       mcon = mycon.connect(host='127.0.0.1', user='root', password="root")
       cur = mcon.cursor()
       cur.execute("use weather")
       mcon.commit()
       con = f"Select Predictions from data where D_S_name='{city}'"
       cur.execute(con)
       conr = cur.fetchone()

       des = f"Select description from data where D_S_name='{city}'"
       cur.execute(des)
       desr = cur.fetchone()

       temp = f"Select temp from data where D_S_name='{city}'"
       cur.execute(temp)
       tempr = cur.fetchone()

       pre = f"Select pressure from data where D_S_name='{city}'"
       cur.execute(pre)
       prer = cur.fetchone()

       hum = f"Select humidity from data where D_S_name='{city}'"
       cur.execute(hum)
       humr = cur.fetchone()

       wind = f"Select wind_speed from data where D_S_name='{city}'"
       cur.execute(wind)
       windr = cur.fetchone()

       if desr==None:
           messagebox.showerror("Weather App", "Sorry! Data is not available \n It will be available Soon!!")
       else:
           t.config(text=(tempr, "°"))
           c.config(text=(conr, "|", "FEELS", "LIKE", tempr, "°"))
           w.config(text=(windr, "m/s"))
           h.config(text=(humr, "%"))
           d.config(text=desr)
           p.config(text=(prer, "hPa"))

image_icon=PhotoImage(file="image/logo.png")
root.iconphoto(False,image_icon)

si=PhotoImage(file="image/Untitled.png")
myimage=Label(image=si,bg="#57adff")
myimage.place(x=20,y=20)

textf=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#131414",border=0,fg="white")
textf.place(x=50,y=40)
textf.focus()

sicon=PhotoImage(file="image/search_icon.png")
myimage_icon=Button(image=sicon,borderwidth=0,cursor="hand2",bg="#131414",command=getweather)
myimage_icon.place(x=400,y=34)

logoi=PhotoImage(file="image/logo.png")
logo=Label(image=logoi,bg="#57adff")
logo.place(x=200,y=100)

fi=PhotoImage(file="image/box.png")
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
timezone.place(x=720,y=33)

long1=Label(root,font=("Helvetica",10),fg="white",bg="#57adff")
long1.place(x=730,y=70)

exit_button = tk.Button(root,font=("arial",15,"bold"),bg="#57adff",borderwidth=0,cursor="hand2", text="Exit", command=exit_application)
exit_button.place(x=800,y=5)

root.mainloop()
#Thankyou