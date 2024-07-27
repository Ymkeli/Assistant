import requests
        
def get_random_numbers_request(params):
    # Does a GET request on the random number API
    url = "http://www.randomnumberapi.com/api/v1.0/random"
    response = requests.get(url,
                            params = params)
    return response.json()

def get_random_numbers(params):
    # Returns one or more random numbers in a given range as a list
    random_numbers = get_random_numbers_request(params)
    return str(random_numbers)