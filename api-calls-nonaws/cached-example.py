import requests
import valkey
import json

# Initialize Valkey client
cache = valkey.StrictValkey(host="your-valkey-endpoint", port=6379, db=0)

def get_weather_cached(city):
    """Optimized: Cache API response to avoid unnecessary API calls"""
    cache_key = f"weather:{city}"
    
    cached_response = cache.get(cache_key)
    if cached_response:
        return json.loads(cached_response)

    # Fetch from API if not in cache
    url = f"https://api.weather.com/v1/{city}/forecast"
    response = requests.get(url).json()
    
    # Cache the API response for 30 minutes
    cache.setex(cache_key, 1800, json.dumps(response))
    
    return response

print(get_weather_cached("New York"))  # Cached Response (Fast & Cost-Effective)
