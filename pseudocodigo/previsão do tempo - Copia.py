import requests
import tkinter as tk
from PIL import Image, ImageTk

# Obter a chave da API da OpenWeatherMap
API_KEY = "58e865e67ac40b6523e9243e1fe82c9b"

# Configurar a janela
root = tk.Tk()
root.geometry("400x400")
root.title("Previsão do Tempo")

# Configurar as imagens do sol e da lua
sun_img = Image.open("sol.png")
moon_img = Image.open("lua.png")
sun_img = sun_img.resize((100, 100))
moon_img = moon_img.resize((100, 100))
sun_icon = ImageTk.PhotoImage(sun_img)
moon_icon = ImageTk.PhotoImage(moon_img)

# Função para obter a previsão do tempo atual
def get_current_weather():
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    current_weather_label.config(text=f"Tempo atual em {city}: {weather}, Temperatura: {temperature}°C, Sensação térmica: {feels_like}°C")
    get_day_night(data)
    get_sun_moon(data)

# Função para obter a previsão do tempo para os próximos 7 dias
def get_weekly_weather():
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    weather_list = []
    for i in range(0, len(data["list"]), 8):
        weather = data["list"][i]["weather"][0]["description"]
        temperature = data["list"][i]["main"]["temp"]
        date = data["list"][i]["dt_txt"].split()[0]
        weather_list.append(f"{date}: {weather}, Temperatura: {temperature}°C")
    weekly_weather_label.config(text="\n".join(weather_list))

# Criar a janela principal
city_label = tk.Label(root, text="Cidade:")
city_entry = tk.Entry(root)
current_weather_button = tk.Button(root, text="Obter Tempo Atual", command=get_current_weather)
weekly_weather_button = tk.Button(root, text="Obter Previsão Semanal", command=get_weekly_weather)
current_weather_label = tk.Label(root, text="")
weekly_weather_label = tk.Label(root, text="")
day_night_label = tk.Label(root, text="")
sun_moon_label = tk.Label(root, image=None)

city_label.pack()
city_entry.pack()
current_weather_button.pack()
weekly_weather_button.pack()
current_weather_label.pack()
weekly_weather_label.pack()
day_night_label.pack()
sun_moon_label.pack()

# Criar a exibição se é dia ou noite
def get_day_night(data):
    sunrise = data["sys"]["sunrise"]
    sunset = data["sys"]["sunset"]
    current_time = data["dt"]
    if current_time > sunrise and current_time < sunset:
        day_night_label.config(text="Dia")
    else:
        day_night_label.config(text="Noite")
        

def get_sun_moon(data):
    sunrise = data["sys"]["sunrise"]
    sunset = data["sys"]["sunset"]
    current_time = data["dt"]
    if current_time > sunrise and current_time < sunset:
        sun_moon_label.config(image=sun_icon)
    else:
        sun_moon_label.config(image=moon_icon)

root.mainloop()
