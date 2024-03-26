# NOTE: Dictionaries

# A recap on the synax
# Lists use []  E.g. scores = [ "45", "56", "52"]
# Tuples use () E.g. fullname = ("Grace", "M", "Hopper")
# Dictionaries use {} E.g. file_counts = {}

file_counts = { 
    # key: value 
    "jpg":10,
    "txt":14,
    "csv":2,
    "py":23
}

print(file_counts)

# NOTE: How to get the value of a dictionary

print("The number of Python files is: {}".format(file_counts["py"]))

#------------------------------------------------------------------------------

# NOTE: How to update a value in a dictionary

file_counts["py"] = 18
print(file_counts)

#------------------------------------------------------------------------------

# NOTE: How to add a new key to a dictionary

file_counts["rs"] = 51 
print(file_counts)

#------------------------------------------------------------------------------

# NOTE: How to delete a key from a dictionary
# Use the "del" keyword

del file_counts["rs"]
print(file_counts)

#------------------------------------------------------------------------------
