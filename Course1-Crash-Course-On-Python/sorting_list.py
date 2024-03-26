numbers = [4, 6, 2, 7, 1]

# Sort from smallest to largest
numbers.sort()

print(numbers)

# NOTE: What is the difference between sort() and sorted()

# Sort will modify the list that it is executed on. E.g. The original

# Sorted will create a new list, and then sort that new list.
# The order of the original list will not be changed

#------------------------------------------------------------------------------

# NOTE: How to sort a list by the length of each item

names = ["Carlos", "Ray", "Alex", "Kelly"]

print(sorted(names, key=len))

#------------------------------------------------------------------------------
