# NOTE: What is Recursion?

# The repeated application of the same procedure to a smaller problem
# In programming,
# recursion is a way of doing repetitive task
# by having a function call itself.

# A recursive function calls itself usually with a modified parameter,
# until it reaches a specific condition (called the base case).

def factiorial(_n):
    print("Factorial called with " + str(_n))
    # This is the base case
    if _n < 2:
        print("Returning 1")
        return 1
    return _n * factiorial(_n-1)
    print("Returning " + str(result) + " for factorial of " + str(_n) )
    return result

factiorial(4)

# NOTE: Usually a recursive function will follow this structure

# def recursive_function(parameters):
#     if base_case_condition(parameters):
#         return base_case_value
#     recursive_function(modified_parameters)

