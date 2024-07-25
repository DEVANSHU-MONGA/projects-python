from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)
root.config(bg="powder blue")


def getWeather():
    try:
        city = textfield.get()
        if not city:
            raise ValueError("City name cannot be empty")

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        if location is None:
            raise ValueError("City not found")

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # Weather
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=(API__ID)" 
        response = requests.get(api)
        if response.status_code != 200:
            raise ValueError("Weather data not found")

        json_data = response.json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°C"))
        c.config(text=(condition, "|", "FEELS LIKE", temp, "°C"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App", str(e))


textfield = Entry(root, justify="center", width=17, font=("poppins 30 bold"), bg="#404040", border=0, fg="white", bd=6, relief=SUNKEN)
textfield.place(x=50, y=40)
textfield.focus()
search_button = Button(root, text="SEARCH", command=getWeather, width=15, height=2, font="Cascadia 10 bold", bg="#1f6e68", bd=5, fg="white")
search_button.place(x=450, y=40)

# Time
name = Label(root, font=("arial", 15, "bold"), background="powder blue")
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20), background="powder blue")
clock.place(x=30, y=130)

# Labels
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=225, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d", background="powder blue")
t.place(x=400, y=150)
c = Label(font=("arial", 15, 'bold'), background="powder blue")
c.place(x=400, y=250)

w = Label(text=" ... ", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text=" ... ", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=250, y=430)
d = Label(text=" ... ", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=470, y=430)
p = Label(text=" ... ", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()
