class WeatherDataProvider:
    def get_weather_data(self):
        pass

class WeatherFetcher(WeatherDataProvider):
    def get_weather_data(self):
        # Logic to fetch weather data from an API
        return "Sunny"

class WeatherApp:
    def __init__(self, weather_data_provider):
        self.weather_data_provider = weather_data_provider

    def get_current_weather(self):
        weather = self.weather_data_provider.get_weather_data()
        return f"Current weather: {weather}"

# Using Dependency Inversion to inject the weather data provider
fetcher = WeatherFetcher()
app = WeatherApp(weather_data_provider=fetcher)

print(app.get_current_weather())




"""

Ab dekhte hain kaise Dependency Inversion ka use karke is example ko improve kiya ja sakta hai. Hum DIP ka use karke abstraction introduce karenge jisse hum low-level WeatherFetcher ko directly use nahi karenge.

"""