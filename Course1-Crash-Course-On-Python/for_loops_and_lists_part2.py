animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
total_chars_in_list = 0

for animal in animals:
    # Count the number of characters in the name,
    # and then add this to the total
    total_chars_in_list += len(animal)

average_length_of_names = total_chars_in_list / len(animals) 

print("Total characters in list: {}".format(total_chars_in_list))
print("Average length of names: {}".format(average_length_of_names))

#------------------------------------------------------------------------------

#NOTE: How to get the index of an element while going through a list

winners = ["Ashley", "Dylan", "Reese"]

for index, person in enumerate(winners):
    print("{} - {}".format(index, person))

# This will print out:
# 0 - Ashley
# 1 - Dylan
# 2 - Reese

#------------------------------------------------------------------------------
