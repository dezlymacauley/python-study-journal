user_name = "Dezly Macauley"

# Get the length of a string
print(len(user_name))

# How to get the first character in a string
first_letter = user_name[0]
print(str(first_letter))

# How to get the last character in a string
last_character = user_name[-1]
print(f"{last_character}")

# How to get a part of a string (E.g. I want the first four letters of my name)
# 0 is the starting index
# 1 is the ending index
first_three = user_name[0:4]
print(f"{first_three}")

# You can also do this
first_three = user_name[:4]
print(f"{first_three}")

# How to get everything after a specific index. 
# E.g. I want it to get my surname
# [4:] means start at index 6, and get everything after that
# Remember that an empty space counts as a character
surname = user_name[6:]
print(f"{surname}")

# NOTE: Finding the index of the first occurence of a character in a string
lightsaber_code = "rws8t"

if "8" in lightsaber_code:
    where_is_the_8 = lightsaber_code.index("8")
    print(f"{where_is_the_8}")
else:
    print("There is no 8")
