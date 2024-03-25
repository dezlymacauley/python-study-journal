def hint_username(_username):
    if len(_username) < 3:
        print("Username must be 3 characters long")
    else:
        print("Valid username")

# NOTE: How to check if a value is even using the modulo operator (%)

def is_even(_number):
    if _number % 2 == 0:
        # When a return statement is executed, the function exits,
        # so that the code that follows doesn't get executed.
        return True
    return False

# Quotient and Remainder
# E.g 5 % 2
# The quotient is 2. 2 will fit into 5 two times. 
# E.g. 2 x 2 = 4

# The remainder is 1

#------------------------------------------------------------------------------

# NOTE: Else, elif, and else

def username_check(_username):
    if len(_username) < 3:
        print("Username must be at least 3 characters long")
    elif len(_username) > 15:
        print("Username cannot be greate than 15 characters")
    else:
        print("Valid username")

#------------------------------------------------------------------------------
