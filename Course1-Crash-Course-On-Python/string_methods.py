favorite_anime = "Naruto"

print(favorite_anime.upper())
print(favorite_anime.lower())

#------------------------------------------------------------------------------
# This is useful for y/n user inputs

answer = "Yes"

if answer.lower() == "yes":
    print("Sale confirmed")

#------------------------------------------------------------------------------

# Use the stip method to get rid of any white space in the user input
# E.g. "Dezly Macauley " becomes "Dezly Macauley"

answer2 = "Dezly Macauley "
print(f"{len(answer2)}")
print(f"{len(answer2.strip())}")

#------------------------------------------------------------------------------

# Check how many times a letter appears

number_of_e = answer2.count("e")
print(f"{number_of_e}")

#------------------------------------------------------------------------------

# Methods on lists of strings

customer_names = ["Jake", "Bob", "Kim"]

# This will create a string of the names in the list.
# " ".join means that each name will be seperated with a space
formatted_customer_names = " ".join(customer_names)

print(formatted_customer_names)

#------------------------------------------------------------------------------

# How to seperate the words in a single string

message = "This is a message"

words_in_message = message.split()

print(f"{words_in_message}")
# This will print
# ['This', 'is', 'a', 'message']

#------------------------------------------------------------------------------
