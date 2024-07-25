from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Setup the OpenAI client
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

def query_openai(query):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful and overly kind assistant."},
            {"role": "user", "content": query}
            ],
        max_tokens=150,
        temperature=0.7)
    return_message = response.choices[0].message.content.strip()
    return return_message

def query_datetime(query):
    # Use OpenAI to obtain a date-time stamp that is X amount of time from the current time, where X is defined in query
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You will be provided with a date-time stamp with the current time and asked to increment this time by a certain amount. Your task is to provide a new date-time stamp in the same format. Return only the new timestamp and nothing more."},
            {"role": "user", "content": query}
            ],
        max_tokens=150,
        temperature=1)
    return_message = response.choices[0].message.content.strip()
    return return_message