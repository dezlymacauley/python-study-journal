# NOTE: A basic function

from re import search


def greeting(_name):
    print("Welcome, " + _name)

greeting("Dezly")

#------------------------------------------------------------------------------

# NOTE: A function will accept multiple parameters

def greeting2(_name, _department):
    print("Welcome " + _name)
    print("You are part of the " + _department + " department")

greeting2("Dezly", "Systems Programming") 

#------------------------------------------------------------------------------

# NOTE: A function that returns a value

def area_of_triangle(_base, _height):
    return (_base * _height)/2

purple_triangle = area_of_triangle(5,4)
green_triangle = area_of_triangle(7,3)

sum_triangle = purple_triangle + green_triangle

print(str(sum_triangle))

#------------------------------------------------------------------------------

# NOTE: A function that returns multiple values

def convert_seconds(_seconds):
    # // means floor division or integer divison
    # It only returns the integer part
    # E.g. 5 // 2 = 2 (not 2.5)
    hours = _seconds // 3600
    minutes = (_seconds - hours * 3600) // 60
    remaining_seconds = _seconds - hours * 3600 - minutes * 60
    
    # This function returns 3 values
    return hours, minutes, remaining_seconds

# Three variables have been created to store each of the three values
user_hours, user_minutes, user_seconds = convert_seconds(5000)

print(hours, minutes, _seconds)

#------------------------------------------------------------------------------
