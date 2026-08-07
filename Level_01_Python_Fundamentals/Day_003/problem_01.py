"""
Problem

Ask the user to enter their age.

Display:

Eligible to Vote

or

Not Eligible to Vote

Example:

Input : 20

Output :

Eligible to Vote

Constraints:
-Age must be between 0 and 120.

Edge Cases:
-Negative age
-Age > 120
-Exactly 18

Hints:
-Use if-else.
-Validate the age before checking eligibility.
"""

#Reading user age
age = int(input("Enter your age: "))

while True:
    # Validating the entered age is between 0-120
    if age < 0 or age > 120:
        print("Invalid input please try again")
        age = int(input("Enter your age: "))

    else : break

# Checking the eligibility
if age >= 18 :
    print("Eligible to Vote")
    

else:
    print("Not Eligible to Vote")
    
