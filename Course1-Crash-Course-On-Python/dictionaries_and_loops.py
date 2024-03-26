file_counts = { 
    # key: value 
    "jpg":10,
    "txt":14,
    "csv":2,
    "py":23
}

for file_extension in file_counts:
    print(file_extension)

# This will print the keys of the dictionary:
# jpg
# txt
# csv
# py

#------------------------------------------------------------------------------

# NOTE: How to print the amounts stored by each key

for file_extension, number_of_files in file_counts.items():
    print("There are {} files with the .{} file extension"
          .format(number_of_files, file_extension))

#------------------------------------------------------------------------------

# NOTE: How to get a list of the keys in a dictionary

print(file_counts.keys())
# dict_keys(['jpg', 'txt', 'csv', 'py'])

for key in file_counts.keys():
    print(key)

#------------------------------------------------------------------------------

# NOTE: How to get a list of values in a dictionary

print(file_counts.values())
# dict_values([10, 14, 2, 23])

for value in file_counts.values():
    print(value)

#------------------------------------------------------------------------------
