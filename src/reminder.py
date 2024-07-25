from open_ai import query_datetime
from datetime import datetime
import threading
import re

def remind(label):
    print("Reminder: " + label)
    
def set_reminder_at(target_time, label):
    now = datetime.now()
    time_diff = (target_time - now).total_seconds()
    timer = threading.Timer(time_diff, lambda: remind(label))
    timer.start()
    
def is_datetime_stamp(string):
    match = re.search("\\d{2}-\\d{2}-\\d{4} \\d{2}:\\d{2}:\\d{2}", string)
    return match != None

def set_reminder(query):
    # Sets a reminder at the time provided in query
    print("Assistant: What label do you want to give your reminder?")
    reminder_label = input("You: ")
    
    # Concat the current date and time to the user query
    now = datetime.now()
    query = now.strftime('%d-%m-%Y %H:%M:%S') + query
    
    response = query_datetime(query)
    
    # First, check if the response is a datetime object.
    # If so, set a reminder. Else, ask for a new query.
    if is_datetime_stamp(response):       
        # Translate the reponse to a date-time object
        format = "%d-%m-%Y %H:%M:%S"
        datetime_object = datetime.strptime(response, format)
        set_reminder_at(datetime_object, reminder_label)
        return f"A reminder has been set at {response}."
    else: 
        return f"I could not set a reminder. Can you reformulate your query?"