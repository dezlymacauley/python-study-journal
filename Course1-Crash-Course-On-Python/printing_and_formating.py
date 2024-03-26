#------------------------------------------------------------------------------

# NOTE: Basic Variable Types

# bool() | boolean | True or False
is_online = False

# str() | string | Any collection of characters that you put in quotes  
user_name = "Luca"
my_message = "I have been living in Argentina for 2 years."

# int() | integers | Any number with no decimals
instagram_followers = 500

# float() | floating point | Any number with decimals 
clothing_expense = 532.65

# None | Used when you want to explicity state that a variable has no value 
current_password = None
database_connection = None

#------------------------------------------------------------------------------

# NOTE: How to explicitly convert one variable type into another

# str(Name of the variable, or value that you want to convert to a str)
# bool(Name of the variable, or value that you want to convert to a bool)
# int(Name of the variable, or value that you want to convert to an int)
# float(Name of the variable, or value that you want to convert to a float)

#------------------------------------------------------------------------------

# NOTE: How to format a string that contains a variable when printing it


#------------------------------------------------------------------------------

# NOTE: Method 1: Explict type conversion
print(user_name + " has " + str(instagram_followers) + " followers on IG")

#------------------------------------------------------------------------------

# NOTE: Method 2: "f string" syntax
# This is the easiest and modern way
print(f"{user_name} has {instagram_followers} followers on IG")

#------------------------------------------------------------------------------

# NOTE: Method 3: The most similar to Rust and C programming

print("{} has {} followers on IG".format(user_name,instagram_followers))

# NOTE: How to format decimals in a string

price = 7.5

tax_cost = price * 1.09 

print(price, tax_cost)

# {:.2f} means display as 2 decimal places
print("Base price is: {:.2f} USD, Tax cost is: {:.2f} USD".format(price,tax_cost))

# You can also adjust the aligment.
# E.g. Center the username 100 spaces
print("{:^100}".format(user_name))

# E.g. align left by 100 spaces
print("{:<100}".format(user_name))

# E.g. align right by 100 spaces
print("{:>100}".format(user_name))

#------------------------------------------------------------------------------
