food_list = ["Milk", "Chocolate", "Egg"]

print(len(food_list))

has_egg = "Egg" in food_list
print(f"{has_egg}")

print(f"{food_list[1]}")

#------------------------------------------------------------------------------

# NOTE: How to add an item to a list
food_list.append("Apple")
print(f"{food_list}")

#------------------------------------------------------------------------------

# NOTE: How to add an item at a specific index

# This will add "Orange" to the start of the list
food_list.insert(0, "Orange")
print(f"{food_list}")

#------------------------------------------------------------------------------

# NOTE: How to remove an element from the end of a list

food_list.remove("Milk")
print(f"{food_list}")

#------------------------------------------------------------------------------

# NOTE: How to remove an element from a specific point in the list

# ['Orange', 'Chocolate', 'Egg', 'Apple']

food_list.pop(2)
print(f"{food_list}")

# This will remove the element at index 2 "Egg"

#------------------------------------------------------------------------------

# NOTE: How to change an item in the list

# ['Orange', 'Chocolate', 'Apple']
food_list[1] = "Cheese Cake"
print(f"{food_list}")

#------------------------------------------------------------------------------
