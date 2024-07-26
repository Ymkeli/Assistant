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

# Description of the random numbers function to use as a tool
tool = {"type": "function",
        "function": {"name": "get_random_numbers",
                     "description": "Generates a list of random numbers",
                     "parameters": {"type": "object",
                                    "properties": {"min": {"type": "integer",
                                                           "description": "the lower end of the input range"},
                                                   "max": {"type": "integer",
                                                            "description": "the higher end of the input range"},
                                                   "count": {"type": "integer",
                                                             "description": "the number of random integers requested"}
        }}}}

def query_random_number_api(query):
    # Use openAI to create the paramaters for a random number request
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You will be asked for one or more random numbers in a specific range. Create the parameters for a function call for the random number api."},
            {"role": "user", "content": query}
            ],
        max_tokens=150,
        temperature=1,
        tools = [tool]
    )
    response_function = response.choices[0].message.tool_calls[0].function
    return response_function