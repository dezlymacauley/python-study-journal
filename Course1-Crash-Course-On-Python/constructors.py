# NOTE: How constructors work

class Apple:
    # __init__ is a constructor function
    # This is a special method that is automatically called,
    # when a class is created.
    # A constructor does two things:
    # 1. It creates the fields for the attributes of a class
    # 2. It simulataneously allows you to add values to those fields  

    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    # E.g. In this example the class is "Apple"
    # This class contains two attributes. "color" and "flavor"

    # NOTE: How to print all the fields and values, 
    # of an instance created with a class when the print method is used

    # Another function needs to be created within the class

    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

#------------------------------------------------------------------------------

# NOTE: Using the constructor when creating a new instance of the class

# jonagold is a variable. The variable type is the Apple class
# Because it follows this variable type, it must have a "color" and "flavor" 
# So jonagold.color = "red" and jonagold.flavor = "sweet"
jonagold = Apple("red", "sweet")

print(jonagold.color)
print(jonagold.flavor)

print(jonagold)
# This apple is red and its flavor is sweet

#------------------------------------------------------------------------------
