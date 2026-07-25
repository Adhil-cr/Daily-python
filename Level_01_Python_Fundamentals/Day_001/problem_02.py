"""
Problem 2 — Basic Calculator

Ask for two integers.

Print:

Sum:
Difference:
Product:
Quotient:

Handle division by zero gracefully.
"""

number_one = int(input("Two numbers : "))
number_two = int(input())

# Sum of two numbers
sum = (number_one + number_two) 
print(f"Sum of two numbers : {sum}") 

# Difference of two numbers
difference = (number_one - number_two)
print(f'Substraction of two numbers : {difference}')

# Product of two numbers
product = (number_one * number_two)
print(f'Multiplication of two number: {product}')

# Quotient of two numbers
Quotient = (number_one / number_two)
print(f'Division of two number: {Quotient}')