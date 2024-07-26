from open_ai.requests import query_datetime, query_random_number_api
from unittest.mock import MagicMock
import open_ai.tools

def mock_response(content):
    # Mock the response of the open AI API. 
    mock_message = MagicMock()
    mock_message.content = content
    
    mock_choice = MagicMock()
    mock_choice.index = 0
    mock_choice.message = mock_message
    
    mock_response = MagicMock()
    mock_response.choices = [mock_choice]
    mock_response.object = "chat.completion"
    return mock_response

def mock_response_function(name, arguments):
    # Mock the response of the open AI API with the tools option
    mock_function = MagicMock()
    mock_function.arguments = str(arguments)
    mock_function.name = name
    
    mock_tool_call = MagicMock()
    mock_tool_call.index = 0
    mock_tool_call.function = mock_function
    
    mock_message = MagicMock()
    mock_message.tool_calls = [mock_tool_call]
    
    mock_choice = MagicMock()
    mock_choice.index = 0
    mock_choice.message = mock_message
    
    mock_response = MagicMock()
    mock_response.choices = [mock_choice]
    mock_response.object = "chat.completion"
    return mock_response

def test_query_datetime(mocker):
    # Mock the response of open AI API
    mock_create = mocker.patch('open_ai.requests.client.chat.completions.create')
    mock_create.return_value = mock_response("24-07-2024 15:00:32")
    
    # Query API
    query = "24-07-2024 14:50:32 Can you set a reminder in 10 minutes?"
    result = query_datetime(query)

    # Assert that the response satisfies expectations
    assert result == "24-07-2024 15:00:32"
    mock_create.assert_called_once_with(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You will be provided with a date-time stamp with the current time and asked to increment this time by a certain amount. Your task is to provide a new date-time stamp in the same format. Return only the new timestamp and nothing more."},
            {"role": "user", "content": query}
        ],
        max_tokens=150,
        temperature=1
    )
    
def test_query_random_number_api(mocker):
    # Mock the response of open AI API
    mock_create = mocker.patch('open_ai.requests.client.chat.completions.create')
    mock_create.return_value = mock_response_function('get_random_numbers',
                                                      [43,66])

    # Query API
    query = "Can you return ro random numbers between 1 and 100?"
    result = query_random_number_api(query)
    print(result)

    # Assert that the response satisfies expectations
    assert result.name == 'get_random_numbers' 
    assert result.arguments == "[43, 66]"
    mock_create.assert_called_once_with(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You will be asked for one or more random numbers in a specific range. Create the parameters for a function call for the random number api."},
            {"role": "user", "content": query}
            ],
        max_tokens=150,
        temperature=1,
        tools = [open_ai.tools.random_numbers]
    )