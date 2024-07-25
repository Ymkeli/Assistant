from reminder import is_datetime_stamp

def test_is_datetime_stamp():
    assert is_datetime_stamp("") == False
    assert is_datetime_stamp("24-7-2024 14:50:32") == False
    assert is_datetime_stamp("24-7-202414:50:32") == False
    assert is_datetime_stamp("24-07-2024 14:50:32") == True