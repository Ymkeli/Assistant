from openai import OpenAI
import openmeteo_requests
from datetime import datetime
import requests_cache
from retry_requests import retry
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Setup the OpenAI client
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

def respond_to_query(query):
    # Call OpenAI's API to get a response
    response = client.chat.completions.create(model="gpt-4o-mini",  
    messages=[
        {"role": "system", "content": "You are a helpful and overly kind assistant."},
        {"role": "user", "content": query}
    ],
    max_tokens=150,
    temperature=0.7)
    return response.choices[0].message.content.strip()

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
        else:
            response = respond_to_query(user_query)

        print(f"Assistant: {response}")