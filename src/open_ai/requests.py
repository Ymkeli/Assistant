from openai import OpenAI
from dotenv import load_dotenv
import os
import open_ai.tools as tools

# Load environment variables from .env file
load_dotenv()

# Setup the OpenAI client
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

def query_open_ai(query):
    # Use openAI to answer the query, or to make the right function call.
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. You help by returning the right function and arguments corresponding to the question. If there is no function that matches the question, you answer by your own knowledge."},
            {"role": "user", "content": query}
            ],
        max_tokens=150,
        temperature=1,
        tools = [tools.random_numbers,
                 tools.current_time,
                 tools.reminder,
                 tools.weather]
    )
    return response.choices[0].message
