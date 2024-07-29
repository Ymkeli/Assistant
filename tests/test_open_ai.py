from open_ai.requests import query_open_ai, assistant_prompt
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

def test_query_open_ai(mocker):
    """TEST 1 - Open AI call that returns content"""
    # Mock the response of open AI API
    mock_create = mocker.patch('open_ai.requests.client.chat.completions.create')
    mock_create.return_value = mock_response("A spider has eight legs.")
    
    # Query API
    query = "How many legs does a spider have?"
    messages = [assistant_prompt, {"role": "user", "content": query}]
    result = query_open_ai(messages)
    first_request_response = result.content

    # Assert that the response satisfies expectations
    assert first_request_response == "A spider has eight legs."
    mock_create.assert_called_once_with(
        model="gpt-4o-mini",
        messages=[assistant_prompt,
                  {"role": "user", "content": "How many legs does a spider have?"}],
        max_tokens=150,
        temperature=1,
        tools = [open_ai.tools.random_numbers,
                 open_ai.tools.current_time,
                 open_ai.tools.reminder,
                 open_ai.tools.weather]
    )
    # Add response message to the message history
    messages.append({"role": "system",
                     "content": first_request_response})
    
    """TEST 2 - Open AI call that returns a tool"""
    # Mock the response of open AI API
    mock_create = mocker.patch('open_ai.requests.client.chat.completions.create')
    mock_create.return_value = mock_response_function('get_random_numbers',
                                                      [43,66])

    # Query API
    query = "Can you return ro random numbers between 1 and 100?"
    messages.append({"role": "user", "content": "Can you return ro random numbers between 1 and 100?"})
    result = query_open_ai(messages)

    # Assert that the response satisfies expectations
    assert result.tool_calls[0].function.name == 'get_random_numbers' 
    assert result.tool_calls[0].function.arguments == "[43, 66]"
    mock_create.assert_called_once_with(
    model="gpt-4o-mini",
    messages= [assistant_prompt,
               {"role": "user", "content": "How many legs does a spider have?"},
               {"role": "system", "content": first_request_response},
               {"role": "user", "content": "Can you return ro random numbers between 1 and 100?"}],
    max_tokens=150,
    temperature=1,
    tools = [open_ai.tools.random_numbers,
             open_ai.tools.current_time,
             open_ai.tools.reminder,
             open_ai.tools.weather]
    )