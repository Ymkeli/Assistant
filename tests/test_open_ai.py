from open_ai import query_datetime
from unittest.mock import MagicMock

def test_query_datetime(mocker):
    mock_create = mocker.patch('open_ai.client.chat.completions.create')
    
    # Mock the response of the open AI API. 
    # Note that the API returns a chat completion object.
    mock_message = MagicMock()
    mock_message.content = "24-07-2024 15:00:32"
    
    mock_choice = MagicMock()
    mock_choice.index = 0
    mock_choice.message = mock_message
    
    mock_response = MagicMock()
    mock_response.choices = [mock_choice]
    mock_response.object = "chat.completion"
    mock_create.return_value = mock_response
    
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