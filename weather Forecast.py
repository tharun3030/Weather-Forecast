import tkinter as tk
from tkinter import messagebox
import requests
import time

# Global variables to track unit state and weather data
is_celsius = True
weather_data = {}


def getWeather():
    global weather_data, is_celsius
    city = textField.get().strip()

    if not city:
        messagebox.showerror("Input Error", "Please enter a city name")
        return

    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=06c921750b9a82d8f5d1294e1586276f"

    try:
        json_data = requests.get(api).json()

        if json_data.get('cod') != 200:
            messagebox.showerror("Error", f"City '{city}' not found.")
            return

        # Store the weather data for easy toggling between units
        weather_data = {
            'condition': json_data['weather'][0]['main'],
            'temp': json_data['main']['temp'],  # Kelvin
            'min_temp': json_data['main']['temp_min'],
            'max_temp': json_data['main']['temp_max'],
            'pressure': json_data['main']['pressure'],
            'humidity': json_data['main']['humidity'],
            'wind': json_data['wind']['speed'],
            'sunrise': json_data['sys']['sunrise'],
            'sunset': json_data['sys']['sunset'],
        }

        # Update the display with the current unit (Celsius by default)
        update_display()

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")


def update_display():
    global is_celsius, weather_data

    if not weather_data:
        return

    # Temperature conversion
    if is_celsius:
        temp = int(weather_data['temp'] - 273.15)
        min_temp = int(weather_data['min_temp'] - 273.15)
        max_temp = int(weather_data['max_temp'] - 273.15)
    else:
        temp = int((weather_data['temp'] - 273.15) * 9 / 5 + 32)
        min_temp = int((weather_data['min_temp'] - 273.15) * 9 / 5 + 32)
        max_temp = int((weather_data['max_temp'] - 273.15) * 9 / 5 + 32)

    pressure = weather_data['pressure']
    humidity = weather_data['humidity']
    wind = weather_data['wind']
    sunrise = time.strftime('%I:%M:%S %p', time.gmtime(weather_data['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S %p', time.gmtime(weather_data['sunset'] - 21600))

    # Update labels
    final_info = f"Condition: {weather_data['condition']}\nTemperature: {temp}°{'C' if is_celsius else 'F'}"
    final_data = (
        f"Min Temp: {min_temp}°{'C' if is_celsius else 'F'}\nMax Temp: {max_temp}°{'C' if is_celsius else 'F'}\n"
        f"Pressure: {pressure} hPa\nHumidity: {humidity}%\n"
        f"Wind Speed: {wind} m/s\nSunrise: {sunrise}\nSunset: {sunset}")

    label1.config(text=final_info)
    label2.config(text=final_data)


def toggle_units():
    global is_celsius
    is_celsius = not is_celsius
    units_button.config(text="Switch to Fahrenheit" if is_celsius else "Switch to Celsius")
    update_display()


# Initialize UI
canvas = tk.Tk()
canvas.geometry("600x600")
canvas.title("Weather App")
canvas.config(bg="lightblue")

f = ("poppins", 15, "bold")
t = ("poppins", 25, "bold")

# Input field
textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()

# Button to get weather
fetch_button = tk.Button(canvas, text="Get Weather", font=f, command=getWeather, bg="orange")
fetch_button.pack(pady=10)

# Toggle units button
units_button = tk.Button(canvas, text="Switch to Fahrenheit", font=f, command=toggle_units, bg="white")
units_button.pack(pady=10)

# Weather information labels
label1 = tk.Label(canvas, font=t, bg="white")
label1.pack()
label2 = tk.Label(canvas, font=f, bg="lightblue")
label2.pack()

canvas.mainloop()
