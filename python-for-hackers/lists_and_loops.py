# NOTE: This data structure is called a `list` 

fruits = ["apple", "banana", "cherry"]

for value in fruits:
    print(f"This sweet is {value} flavoured")

# NOTE: When using the `range` in Python, remember that the second number is,
# excluded! range(1,11) mean 1 to 10
# The last number at the end (the 1), 
# means move through the list in steps of 1

for value in range(1,11,1):
    print(f"{value}")

for value in range(1,25):
    if value % 3 == 0:
        print(f"{value} is divisible by three")
