from datetime import datetime
from reminder import set_reminder
from open_ai.requests import query_open_ai, assistant_prompt
from random_numbers import get_random_numbers
from weather import get_weather
import json

def get_current_time():
    now = datetime.now()
    return f"The current time is {now.strftime('%H:%M:%S')}."

if __name__ == "__main__":
    print("Hello! I'm your personal assistant. How can I help you today?")
    # Save all chat messages in the message history
    message_history = [assistant_prompt]
    
    while True:
        user_query = input("You: ")
        if user_query.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        
        message_history.append({"role": "user", "content": user_query})
        openai_response = query_open_ai(message_history)
        
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
            # Add the function response to the message history        
            message_history.append({"role": "function",
                                            "name": f_response.name,
                                            "content": response})
        else:
            response = openai_response.content
            message_history.append({"role": "system", 
                                    "content": response})
                
        print(f"Assistant: {response}")