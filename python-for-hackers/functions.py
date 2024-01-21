# NOTE: Unlike Rust, in Python, 
# functions must be defined before you use them.

def say_hello():
    print("Hello")

say_hello()

# num1 and num2 are called parameters
def sum_of_two_numbers(num1,num2):
    sum = num1 + num2
    print(f"{sum}")

num1 = int(input("What is the first number you want to add? "))
num2 = int(input("What is the second number you want to add? "))

sum_of_two_numbers(num1,num2)
