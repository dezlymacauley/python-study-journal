# NOTE: Final Project

#------------------------------------------------------------------------------

# NOTE: Functions that the main program will use

def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}

    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":  # Changed "=" to "=="
            machines[event.machine].add(event.user)
        elif event.type == "logout":  
            machines[event.machine].remove(event.user)
    return machines  

def generate_report(machines):
    for machine, users in machines.items():  
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

#------------------------------------------------------------------------------

# NOTE: The main program

class Event:
    # __init__ is a constructor function
    # This constructor function will set the necessary events
    def __init__(self, even_date, event_type, machine_name, user):
        self.date = even_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

#-----------------------------------------------------------------------------

# NOTE: Sample data

event = [
    Event("2020-01-21 12:45:56", "login", "myworkstation.local", "jordan"),
    Event("2020-01-22 15:53:42", "logout", "webserver.local", "jordan"),
    Event("2020-01-21 18:53:21", "login", "myworkstation.local", "lane"),

    Event("2020-01-21 08:20:01", "login", "webserver.local", "jordan"),
    Event("2020-01-23 11:24:35", "login", "mailserver.local", "chris"),
]

#-----------------------------------------------------------------------------

# NOTE: Using the code

# users = current_users(events)
# print(users)

# generate_report(users)

# This should print out something like:
# webserver.local: lane
# webserver.local: chris

#-----------------------------------------------------------------------------
