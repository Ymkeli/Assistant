from open_ai import query_datetime

def set_reminder(query):
    # Set a reminder at the time provided in query
    # At this moment, this function only returns the correct timestamp
    datetime = query_datetime(query)
    return f"A reminder has been set at {datetime}."