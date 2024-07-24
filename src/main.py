import openmeteo_requests
from datetime import datetime
import requests_cache
from retry_requests import retry
from reminder import set_reminder
from open_ai import query_openai

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

def get_current_time():
    now = datetime.now()
    return f"The current time is {now.strftime('%H:%M:%S')}."

def get_weather():
    # Call OpenMeteo's API to get the current temperature for Utrecht
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": 52.091259,
              "longitude": 5.122750,
              "current": "temperature_2m"}
    response = openmeteo.weather_api(url, params=params)
    current_temp = round(response[0].Current().Variables(0).Value(),2)
    return f"The current temperature in Utrecht is {current_temp} degrees."

if __name__ == "__main__":
    print("Hello! I'm your personal assistant. How can I help you today?")
    while True:
        user_query = input("You: ")
        if user_query.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        if 'time' in user_query.lower():
            response = get_current_time()
        elif 'weather' in user_query.lower():
            response = get_weather()
        elif 'reminder' in user_query.lower():
            response = set_reminder(user_query)
        else:
            response = query_openai(user_query)

        print(f"Assistant: {response}")