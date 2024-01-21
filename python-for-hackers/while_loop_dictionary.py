# First I will start off with a dictionary to that will add a student name,
# and their grade.

student_grades = {}

done_with_entries = False

while not done_with_entries:
    # First get the student name and grade and save it to a variable
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")

    # Next save it to the dictionary
    student_grades[name] = grade
    print(f"{name} and the grade of {grade} has been added sucessfully")
    i_want_to_continue = input("Would you like to add another student? y or n ").lower()
    
    if i_want_to_continue == "y":
        pass # Restart the loop and ask for the name of the next student
    else:
        done_with_entries = True;

print(student_grades)
