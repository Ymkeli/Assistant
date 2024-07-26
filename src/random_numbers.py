import requests
import json
from open_ai.requests import query_random_number_api
        
def get_random_numbers_request(params):
    # Does a GET request on the random number API
    url = "http://www.randomnumberapi.com/api/v1.0/random"
    response = requests.get(url,
                            params = params)
    return response.json()

def get_random_numbers(query):
    # Returns one or more random numbers in a given range as a list
    function = query_random_number_api(query)
    f_params = json.loads(function.arguments)
    if function.name == 'get_random_numbers':
        answer = get_random_numbers_request(f_params)
        return str(answer)
    else: return "No random number(s) could be generated."