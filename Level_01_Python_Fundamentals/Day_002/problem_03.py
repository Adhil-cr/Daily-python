"""
Problem

A user can log in only if:

Age is at least 18
Email is verified

Read:
Age
Email verified (True or False)

Print:
Access Granted
or
Access Denied

Example: 

Age

22

Verified

True

Output :
Access Granted

Constraints:
-Age between 0 and 120.

Edge Cases:
-Invalid age.
-Different letter cases for true/false.

"""

# Reading Age and Email
age = int(input("Enter your age: "))
verified = input("Enter True/False : ")

if age > 0 and age <=120 :

    verified = verified.lower()

    if age >=18 and verified =="true" :
        print("Access Granted")

    else :
        print("Access Denied")
        
else :
    print("Invalid Age")