# According to the Python style guide,
# a class should start with a capital letter

#------------------------------------------------------------------------------

# NOTE: How to create a class

class Apple:
    color = ""
    flavor = ""

#------------------------------------------------------------------------------

# NOTE: How to create a new instance of a class

jonagold = Apple()

#------------------------------------------------------------------------------

# NOTE: How to set the attributes of that instance

jonagold.color = "red"
jonagold.flavor = "sweet"

print(jonagold.color)
print(jonagold.flavor)

# Because the attributes "color" and "flavor",
# were declared as strings when you designed this class
# They have all the methods that a string class has

print(jonagold.color.upper())

#------------------------------------------------------------------------------

class Piglet:
    animal_name = ""
    years = 0
    # pass is just a way to tell Python to ignore any missing details
    # move onto the next block of code.
    # Useful for when you are working on something
    # and plan to come back to it soon,
    # but you want to write some other code below

    # pass
    
    # This function is indented because it is a function of the class Piglet
    # "self" means whatever instance that this method is being executed on.
    # E.g. It could be the variable "hamlet"
    # In simple terms.. any variable that is created from the class "Piglet"
    # will be able to use these functions

    def speak(self):
        print("oink oink")
        print("Hi, my name is {}".format(self.animal_name))

    def pig_years(self):
        return self.years * 18

hamlet = Piglet()
hamlet.animal_name = "hamlet"
hamlet.speak()

hamlet.years = 2
hamlet.pig_years()

print(hamlet.pig_years())

#------------------------------------------------------------------------------
