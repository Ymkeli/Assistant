# Description of the random numbers function to use as a tool
random_numbers = {"type": "function",
                  "function": {"name": "get_random_numbers",
                               "description": "Generates a list of random numbers",
                               "parameters": {"type": "object",
                                              "properties": {"min": {"type": "integer",
                                                                     "description": "the lower end of the input range"},
                                                             "max": {"type": "integer",
                                                                     "description": "the higher end of the input range"},
                                                             "count": {"type": "integer",
                                                                       "description": "the number of random integers requested"}
                                                             }}}}