import requests
import customtkinter

YOUR_API_KEY = "a03e85b8d2cb88a5f53b544442f8ab56"
city = "Northwich"

def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={YOUR_API_KEY}"
    params = {
        "units" : "metric"
    }
    response = requests.get(url, params=params)
    return response.json()

def get_temp(city):
    weather_data = get_weather_data(city)
    return weather_data["main"]["temp"]
def get_weather(city):
    weather_data = get_weather_data(city)
    return weather_data["weather"][0]["main"]

class Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = customtkinter.CTkLabel(self)
        self.label.configure(text=f"The temperature is {get_temp(city)}")
        self.label.grid(row=0, column=0, padx=20, pady=20)
        self.l = customtkinter.CTkLabel(self)
        self.l.configure(text=f"The current weather condition: {get_weather(city)}")
        self.l.grid(row=1, column=0, padx=20, pady=20)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame = Frame(master=self)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

app = App()
app.mainloop()