class WeatherFetcher:
    def fetch_weather(self):
        # Logic to fetch weather data from an API
        return "Sunny"

class WeatherApp:
    def __init__(self):
        self.weather_fetcher = WeatherFetcher()

    def get_current_weather(self):
        weather = self.weather_fetcher.fetch_weather()
        return f"Current weather: {weather}"

app = WeatherApp()
print(app.get_current_weather())
