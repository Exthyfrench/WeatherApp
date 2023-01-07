import tkinter as tk
import requests

# OpenWeatherMap API key
api_key = "YOUR_API_KEY_HERE"

# Base URL for the OpenWeatherMap API
base_url = "http://api.openweathermap.org/data/2.5/weather"

# Function to get the weather for a given city
def get_weather(city):
  # Build the URL with the city and API key
  url = f"{base_url}?q={city}&appid={api_key}"
  
  # Send a request to the API and get the response
  response = requests.get(url)
  
  # If the request was successful, parse the JSON data
  if response.status_code == 200:
    data = response.json()
    
    # Extract the relevant data from the JSON
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    
    # Update the GUI with the extracted data
    temperature_label.config(text=f"Temperature: {temperature}°F")
    humidity_label.config(text=f"Humidity: {humidity}%")
    description_label.config(text=description)
  else:
    # If the request failed, display an error message
    temperature_label.config(text="Error")
    humidity_label.config(text="Error")
    description_label.config(text="Error")

# Create the main window
window = tk.Tk()
window.title("Weather App")

# Create a frame for the entry and button
entry_frame = tk.Frame(window)
entry_frame.pack()

# Create an entry for the city name
city_entry = tk.Entry(entry_frame)
city_entry.pack(side="left")

# Create a button to get the weather
get_weather_button = tk.Button(entry_frame, text="Get Weather", command=lambda: get_weather(city_entry.get()))
get_weather_button.pack(side="left")

# Create a frame for the labels
label_frame = tk.Frame(window)
label_frame.pack()

# Create labels to display the weather data
temperature_label = tk.Label(label_frame, text="Temperature:")
temperature_label.pack()

humidity_label = tk.Label(label_frame, text="Humidity:")
humidity_label.pack()

description_label = tk.Label(label_frame, text="Description:")
description_label.pack()

# Run the main loop
window.mainloop()
