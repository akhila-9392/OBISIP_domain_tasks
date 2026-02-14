import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    api_key = "YOUR_API_KEY"  # 1. API Integration: Requires OpenWeatherMap Key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        # 1. Parsing JSON data
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temp_c = data["main"]["temp"]
            # 7. Unit Conversion (Celsius to Fahrenheit)
            temp_f = (temp_c * 9/5) + 32
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]

            res_text = f"Temp: {temp_c}°C / {temp_f:.1f}°F\nHumidity: {humidity}%\nCondition: {condition.capitalize()}"
            weather_info.config(text=res_text)
        else:
            # 5. Error Handling: Invalid City
            messagebox.showerror("Error", "City not found!")
    except Exception as e:
        messagebox.showerror("Error", "Could not connect to API.")

# 3. GUI Design
root = tk.Tk()
root.title("Python Weather App")
root.geometry("300x300")

tk.Label(root, text="Enter City Name:").pack(pady=10)
city_entry = tk.Entry(root)
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)
weather_info = tk.Label(root, text="", font=("Arial", 10, "bold"))
weather_info.pack(pady=20)

root.mainloop()