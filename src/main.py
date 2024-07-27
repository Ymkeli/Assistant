from datetime import datetime
from reminder import set_reminder
from open_ai.requests import query_open_ai
from random_numbers import get_random_numbers
from weather import get_weather
import json

def get_current_time():
    now = datetime.now()
    return f"The current time is {now.strftime('%H:%M:%S')}."

if __name__ == "__main__":
    print("Hello! I'm your personal assistant. How can I help you today?")
    while True:
        user_query = input("You: ")
        if user_query.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        
        openai_response = query_open_ai(user_query)
        if openai_response.content == None:
            f_response = openai_response.tool_calls[0].function
            match f_response.name:
                case 'get_current_time':
                    response = get_current_time()
                case 'get_random_numbers':
                    params = json.loads(f_response.arguments)
                    response = get_random_numbers(params)
                case 'set_reminder':
                    params = json.loads(f_response.arguments)
                    response = set_reminder(params)
                case 'get_weather':
                    params = json.loads(f_response.arguments)
                    response = get_weather(params)
        else:
            response = openai_response.content
                
        print(f"Assistant: {response}")