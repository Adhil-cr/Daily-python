"""
Problem 3 — Age Category

Ask for age.

Print one of:

Child 
Teenager 
Adult 
Senior 

hint :  child (6 to 12 years), 
        teenager (13 to 19 years),
        adult (20 to 64 years), 
        and senior (65 years and older)

Also reject invalid ages:

Age must be between 0 and 120.
"""

# Reading input Age
Age = int(input("Enter the Age: "))

# Checking the age limit using if-else ladder
if Age <= 12 :
    print("Child")
elif Age <= 19:
    print("Teenager")
elif Age <= 64:
    print("Adult")
elif Age <= 120:
    print("Senior")
else:
    print("Invalid Input")



