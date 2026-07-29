"""
Problem

Read two numbers and display the result of every arithmetic operator.

Display:

Addition
Subtraction
Multiplication
Division
Floor Division
Modulus
Exponent

-- Example --

Input:

12
5

Output:

Addition: 17
Subtraction: 7
Multiplication: 60
Division: 2.4
Floor Division: 2
Modulus: 2
Exponent: 248832

Constraints:
-Accept integers only.
-Handle division by zero gracefully.

Edge Cases:
-Second number is 0.
-Negative numbers.

"""

# Reading two numbers

number1 = int(input("Enter an integer number: "))
number2 = int(input("Enter an integer number: "))

while True :
    if number1 == 0  or number2 == 0:
        print("Zero is invalid , please enter other integers")

        number1 = int(input("Enter an integer number: "))
        number2 = int(input("Enter an integer number: "))

    else :
        break


print()
print(f"Addition : {number1 + number2}\n"
        f"Subtraction : {number1 - number2}\n"
        f"Multiplication : {number1 * number2}\n"
        f"Division : {number1 / number2}\n"
        f"Floor Division : {number1 // number2}\n"
        f"Modulus : {number1 % number2}\n"
        f"Exponent : {number1 ** number2}\n")