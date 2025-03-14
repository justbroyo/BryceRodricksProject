import requests

def get_weather(location):
    url = f"https://wttr.in/{location}?format=%C+%t+%T"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.text.split()
        condition, temp_c, temp_f = data[0], data[1], data[2]
        
        # Weather emojis dictionary
        emojis = {
            "Clear": "☀️", "Sunny": "🌞", "Cloudy": "☁️", "Overcast": "☁️",
            "Partly": "⛅", "Rain": "🌧️", "Drizzle": "🌦️", "Thunderstorm": "⛈️",
            "Snow": "❄️", "Mist": "🌫️", "Fog": "🌫️"
        }
        
        # Get the emoji for the weather condition, default to Earth emoji if not found
        emoji = next((emoji for key, emoji in emojis.items() if key in condition), "🌍")
        
        print(f"Weather in {location}: {condition} {emoji}")
        print(f"Temperature: {temp_c}°C ({temp_f}°F)")
    else:
        print("Error fetching weather data. Try again.")

# Get user input for location
location = input("Enter a location: ")
get_weather(location)


