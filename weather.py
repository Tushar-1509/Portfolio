from tkinter import *
from tkinter import ttk
import requests

def get_weather():
    city = com.get()
    if not city:
        return
    api_key = "api key"  # Replace with the actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            w_label1.config(text="N/A")
            w1_label1.config(text="City Not Found")
            temp_label1.config(text="N/A")
            pre_label1.config(text="N/A")
            return

        weather_main = data["weather"][0]["main"]
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        pressure = data["main"]["pressure"]

        w_label1.config(text=weather_main)
        w1_label1.config(text=weather_desc)
        temp_label1.config(text=f"{temp} °C")
        pre_label1.config(text=f"{pressure} hPa")

    except Exception as e:
        w_label1.config(text="Error")
        w1_label1.config(text=str(e))
        temp_label1.config(text="N/A")
        pre_label1.config(text="N/A")

win = Tk()
win.title("Tushar's Weather App")
win.config(bg="skyblue")
win.geometry("500x500")

name_label = Label(win, text="Tushar's Weather App", font=("arial", 20, "italic"), bg="white")
name_label.place(x=107, y=25, height=30, width=280)

indian_cities = [
    "Delhi,IN", "Mumbai,IN", "Kolkata,IN", "Chennai,IN", "Bangalore,IN", "Hyderabad,IN", "Ahmedabad,IN",
    "Pune,IN", "Jaipur,IN", "Lucknow,IN", "Kanpur,IN", "Nagpur,IN", "Indore,IN", "Bhopal,IN", "Patna,IN",
    "Ludhiana,IN", "Agra,IN", "Nashik,IN", "Vadodara,IN", "Faridabad,IN", "Ghaziabad,IN", "Meerut,IN",
    "Rajkot,IN", "Kalyan,IN", "Vasai,IN", "Varanasi,IN", "Srinagar,IN", "Amritsar,IN", "Allahabad,IN",
    "Ranchi,IN", "Coimbatore,IN", "Jodhpur,IN", "Raipur,IN", "Guwahati,IN", "Chandigarh,IN", "Mysore,IN",
    "Jalandhar,IN", "Thiruvananthapuram,IN", "Noida,IN", "Gurgaon,IN", "Howrah,IN", "Solapur,IN",
    "Hubli,IN", "Tiruchirappalli,IN", "Bareilly,IN", "Moradabad,IN", "Gwalior,IN", "Jammu,IN", "Jamshedpur,IN"
]


    

com = ttk.Combobox(win, value=indian_cities, font=("Arial", 15, "bold"))
com.place(x=50, y=100, height=35, width=400)

done_button = Button(win, text="Done", font=("Arial", 15, "bold"), command=get_weather)
done_button.place(x=220, y=150)

w_label = Label(win, text="Weather",bg="skyblue", font=("Arial", 15))
w_label.place(x=50, y=200)
w_label1 = Label(win, text="-",bg="skyblue", font=("Arial", 15))
w_label1.place(x=250, y=200)

w1_label = Label(win, text="Description",bg="skyblue", font=("Arial", 15))
w1_label.place(x=50, y=230)
w1_label1 = Label(win, text="-",bg="skyblue", font=("Arial", 15))
w1_label1.place(x=250, y=230)

temp_label = Label(win, text="Temperature",bg="skyblue", font=("Arial", 15))
temp_label.place(x=50, y=260)
temp_label1 = Label(win, text="-",bg="skyblue", font=("Arial", 15))
temp_label1.place(x=250, y=260)

pre_label = Label(win, text="Pressure",bg="skyblue", font=("Arial", 15))
pre_label.place(x=50, y=290)
pre_label1 = Label(win, text="-",bg="skyblue", font=("Arial", 15))
pre_label1.place(x=250, y=290)

win.mainloop()
