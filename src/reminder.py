from datetime import datetime, timedelta
import threading

def remind(label):
    print("Reminder: " + label)
    
def set_reminder_at(target_time, label):
    now = datetime.now()
    time_diff = (target_time - now).total_seconds()
    timer = threading.Timer(time_diff, lambda: remind(label))
    timer.start()

def set_reminder(params):  
    if "seconds" in params:
        # Sets a reminder in a given number of seconds
        print("Assistant: What label do you want to give your reminder?")
        reminder_label = input("You: ")
    
        # Concat the current date and time to the user query
        reminder_time = datetime.now() + timedelta(seconds= params["seconds"])
        set_reminder_at(reminder_time, reminder_label)
    
        return f"A reminder has been set at {reminder_time}."
    else: 
        return "I couldn't set a timer."