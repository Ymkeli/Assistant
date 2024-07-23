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