# NOTE: The problem

# I need to create a daily report that tracks the use of machines

# Which users are connected to which machines

# There is a system that collects every event that happens on the machines
# It records every time a user logs in or out of a computer

# I need to write a report of which users are logged into which machine,
# during a certain window

# Input = A list of events. Each event is an instance of the "Event" class

# The event class contains the date when the event happened, 
# the name of the machine where it happened, the user involved, 
# and the event type

#------------------------------------------------------------------------------

# NOTE: What attribute does the Event class have?

# Date
# User
# Machine
# Type

# These are all strings

# Login
# Logout

#------------------------------------------------------------------------------

# NOTE: What does the input and ouput look like? 

# Input:
# The script will recieve a list of Event objects

# Output:

# List all the machine names
# The users that are currently logged in

# Machine
# User
# Date
# Type

# E.g.

# E.g. webserver.local:
# Kay, Taylor, Charlie

#------------------------------------------------------------------------------

# NOTE: How do I plan on keeping track on Logins and Logout

# I will be using a "Set"

# Key = Name of machine
# Current user of that machine is the value

#------------------------------------------------------------------------------
