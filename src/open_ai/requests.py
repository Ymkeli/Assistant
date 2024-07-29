from openai import OpenAI
from dotenv import load_dotenv
import os
import open_ai.tools as tools

# Assistant prompt
assistant_prompt = {"role": "system", "content": "You are a helpful assistant. You assist me by calling specific tools to retrieve random numbers, the current time and weather data and to set reminders."}

# Load environment variables from .env file
load_dotenv()

# Setup the OpenAI client
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

def query_open_ai(messages):
    # Use openAI to answer the query, or to make the right function call.
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=150,
        temperature=1,
        tools = [tools.random_numbers,
                 tools.current_time,
                 tools.reminder,
                 tools.weather]
    )
    return response.choices[0].message
