# NOTE: A basic function

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



#------------------------------------------------------------------------------
