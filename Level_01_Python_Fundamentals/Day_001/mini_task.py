"""
Mini Task — Student Information Collector

Collect:

Name
Age
College
Course
Email

Requirements:

Age must be positive.
Empty values are not allowed.
Display a clean summary.
Use descriptive variable names.
Use f-strings.
Stretch Goal

Keep asking until the user enters valid input.
"""

# Reading Student Details
student_name = input("Enter your name:").strip()

while not student_name:
    print("Empty values are not allowed.")
    student_name = input("Enter your name:").strip()
    break


while True:
    student_age = int(input("Enter your age:"))

    if student_age > 0 :
        break

    print("Invalid input! Please enter a positive number.")

college_name = input("Enter your college name:").strip()

while not college_name:
    print("Empty values are not allowed.")
    college_name = input("Enter your college name:").strip()
    break

course_name = input("Enter your course name:").strip()

while not course_name:
    print("Empty values are not allowed.")
    course_name = input("Enter your course name:").strip()
    break

while True:
    email = input("Enter your email: ").strip()

    if "@" in email and "." in email :
        print("Valid email")
        break

    print("Invalid email! please try again")


print(f"Your name is {student_name} and you're {student_age} years old.You are studying {course_name} at {college_name} and your email id is {email}.")