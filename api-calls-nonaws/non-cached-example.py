import requests

def get_weather(city):
    """Calls API every time, even for the same city"""
    url = f"https://api.weather.com/v1/{city}/forecast"
    response = requests.get(url)
    return response.json()

print(get_weather("New York"))  # External API call (Expensive!)
