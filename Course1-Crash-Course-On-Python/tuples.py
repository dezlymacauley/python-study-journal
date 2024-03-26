# NOTE: Tuples

# Tuples are sequences of element of any type that are immutable
# A key syntax difference, is that tuples are declared with () brackets 

# Another major difference is that when using tuples,
# the position of the elements inside the tuple have meaning.
# In a tuple, the order of the elements matters

# Fun fact: When a function returns more than one value, 
# it is actually returning a tuple

fullname = ("Grace", "M", "Hopper")
print(f"{fullname}")
# ('Grace', 'M', 'Hopper')

#------------------------------------------------------------------------------

# NOTE: How to Unpack tuples

# The values in a tuple can be assigned to multiple elements, 
# as long as you pay attention to the order. 

user_name, user_initial, user_surname = fullname

print(user_name)
print(user_initial)
print(user_surname)


#------------------------------------------------------------------------------
