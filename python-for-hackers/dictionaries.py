dictionary = {"name": "Ryan", "age": "30"} 

print(dictionary)
print(dictionary["name"])

# NOTE: How to modify the dictionary
print(dictionary)

dictionary["id"] = "1"

# NOTE: How to print the value of keys in a dictionary

for value in dictionary:
    print(dictionary[value])


# NOTE: How to make a dictionary empty
dictionary = {}
print(dictionary)
