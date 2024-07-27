import openmeteo_requests
import requests_cache
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

def get_weather(location):
    # Call OpenMeteo's API to get the current temperature for Utrecht
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": location["latitude"],
              "longitude": location["longitude"],
              "current": "temperature_2m"}
    response = openmeteo.weather_api(url, params=params)
    current_temp = round(response[0].Current().Variables(0).Value(),2)
    return f"The current temperature in {location["name"]} is {current_temp} degrees."