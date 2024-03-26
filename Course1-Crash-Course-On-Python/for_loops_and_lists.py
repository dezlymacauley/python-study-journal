# NOTE: When to use For Loops vs While Loops

# Use for loops when there's a sequence of elements that you want to iterate.
# Use while loops when you want to repeat an action until a condition changes.

#------------------------------------------------------------------------------

# NOTE: Range Example 1

for x in range(5):
    print(x)

#------------------------------------------------------------------------------

# NOTE: Range Example 2

for n in range(1, 10):
    print("We are at number: " + str(n))

# NOTE: In Python this will print out 1 to 9
# The last number is exclusive

#------------------------------------------------------------------------------

# NOTE: Range Example 2

# The third number means steps. E.g. Go up in steps of two
for n in range(1, 10, 2):
    print("Car number: " + str(n))

# NOTE: In Python this will print out 1, 3, 5, 7, 9
# The last number is exclusive

#------------------------------------------------------------------------------


# NOTE: In Python this will print out 5 numbers, starting from 0!
# I.e. 0 to 4

villains = ["Max", "Taylor", "Jean"]

for villain in villains:
    print("Hi " + villain)

values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0

for value in values:
    sum += value
    length += 1

print("There are " + str(length) +  " numbers in the list")
print("The total is: " + str(sum))
print("The average is: " + str(sum/length))



