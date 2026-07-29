"""
Problem

Read three integers.

Print:

Largest number
Smallest number
Whether all three numbers are equal
Whether at least one number is negative

Example:

Input :
5
9
5

Output :

Largest: 9
Smallest: 5
All Equal: False
Contains Negative: False

Constraints:
-Integer input.

Edge Cases:
- All equal.
- All negative.
- Two equal.

"""

# Reading 3 integers

number1 = int(input("Enter an integer: "))
number2 = int(input("Enter an integer: "))
number3 = int(input("Enter an integer: "))
negative_number = False

# Finding largest and smallest
# If A greater than B
if number1 > number2:

    # If A greater than C
    if number1 > number3:
        # Prints A is Largest
        print(f'Largest:{number1}')

        # If C greater than B
        if number3 > number2 :
            # Prints B is Smallest
            print(f'Smallest:{number2}')

        # If B greater than C
        else :
            # Prints C is Smallest
            print(f'Smallest:{number3}')

    # If C is greater than A
    else:
        # Prints C is Largest
        print(f'Largest:{number3}')
        print(f'Smallest:{number2}')

# If B is greater than A
else :
    # If B is greater than C
    if number2 > number3:
        # Prints B is Largest
        print(f'Largest:{number2}')

        # If C is greater than A
        if number3 > number1:
            # Prints A is Smallest
            print(f"Smallest:{number1}")

        # If A is greater than C
        else:
            # Prints C is Smallest
            print(f"Smallest:{number3}")
        
    else:
        print(f'Largest:{number3}')
        print(f'Smallest:{number1}')


# Checking all three numbers are equal
if number1 == number2 :
    
    if number1 == number3:
        print("All Equal: True")
    else:
        print("All Equal: False")
    
else:
    
    print("All Equal: False")


# Checking negative numbers
if number1 < 0:
    negative_number = True

elif number2 < 0:
    negative_number = True

elif number3 < 0:
    negative_number = True

if negative_number == True:
    print("Contains Negative: True")
else :
    print("Contains Negative: False")