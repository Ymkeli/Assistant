# Descriptions of all tools used in open AI API calls
random_numbers = {"type": "function",
                  "function": {"name": "get_random_numbers",
                               "description": "generates a list of random numbers",
                               "parameters": {"type": "object",
                                              "properties": {"min": {"type": "integer",
                                                                     "description": "the lower end of the input range"},
                                                             "max": {"type": "integer",
                                                                     "description": "the higher end of the input range"},
                                                             "count": {"type": "integer",
                                                                       "description": "the number of random integers requested"}
                                                             }}}}

current_time = {"type": "function",
                "function": {"name": "get_current_time",
                             "description": "returns the current time"}
                }

reminder = {
    "type": "function",
    "function": {
        "name": "set_reminder",
        "description": "set a reminder at a given point in time",
        "parameters": {"type": "object",
                       "properties": {"seconds": {"type": "integer",
                                                  "description": "the number of seconds from now at which the reminder must be set"}
            }}}}

weather = {"type": "function",
           "function": {"name": "get_weather",
                        "description": "returns the current temperature at a given location",
                        "parameters": {"type": "object",
                                       "properties": {"latitude": {"type": "integer",
                                                                   "description": "the latitude of the query location"},
                                                      "longitude": {"type": "integer",
                                                                    "description": "the logintude of the query location"},
                                                      "name": {"type": "string",
                                                               "description": "name of the query location"}},
                                       "required": ["latitude", "longitude", "name"]}}}