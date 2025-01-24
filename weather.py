import requests
import json
from datetime import datetime
import argparse

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_location_weather(self, city):
        try:
            # Make API request
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  # For Celsius
            }
            
            response = requests.get(self.base_url, params=params)
            weather_data = response.json()
            
            if response.status_code == 200:
                # Format weather information
                return f"""
Weather in {weather_data['name']}, {weather_data.get('sys', {}).get('country', '')}
═════════════════════════════════
Temperature: {weather_data['main']['temp']}°C
Feels like: {weather_data['main']['feels_like']}°C
Humidity: {weather_data['main']['humidity']}%
Weather: {weather_data['weather'][0]['description'].capitalize()}
Wind Speed: {weather_data['wind']['speed']} m/s
Pressure: {weather_data['main']['pressure']} hPa
                """
            else:
                return f"Error: Could not fetch weather data. {weather_data.get('message', '')}"
                
        except Exception as e:
            return f"Error occurred: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description='Get weather forecast for a city')
    parser.add_argument('city', help='Name of the city')
    parser.add_argument('--api-key', help='OpenWeatherMap API key', required=True)
    
    args = parser.parse_args()
    
    weather_app = WeatherApp(args.api_key)
    print(weather_app.get_location_weather(args.city))

if __name__ == "__main__":
    main()
