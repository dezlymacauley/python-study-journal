x = 15
y = 15

if x > 15:
    print("X is bigger than y")
elif x < y:
    print("X is smaller than y")
else:
    print("The numbers are the same")

# NOTE: How to make a nested if statement in Python

# The input of the users's score is converted to an integer.
# Then that integer is stored in the variable `score`
score = int(input("What is your score? "))

if score >= 90:
    age = int(input("What is your age? "))
    if age < 12:
        print(input(f"A score of {score} at age {age}! Clearly a prodigy"))
    else:
        print("Well done")
elif score >= 70:
    print("Not bad")
else:
    print("Study more")


