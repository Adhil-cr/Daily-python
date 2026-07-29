"""
Problem

Read an integer and determine whether it is:

Even
Odd

Use the modulus operator.

Example:

Input : 17

Output :

Odd

Constraints:
- Integer input.

Edge Cases:
- 0
- Negative numbers

"""
# Reading input integer
number1 = int(input("Enter an integer number :"))

while True :
    
    if number1 < 0 :
        print("Invalid input! Negative numbers are not allowed")
        number1 = int(input("Enter an integer number :"))
    else :
        break

if number1 % 2 == 0:
    print(f"{number1} is Even")
else :
    print(f"{number1} is Odd")   