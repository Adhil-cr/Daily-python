'''
Problem : Create a calculator that repeatedly displays:

===== Calculator =====
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Ask the user to select an option.

For options 1–4:

Ask for two numbers.
Perform the selected operation.
Display the result.
Return to the menu.

For option 5:

Goodbye!and terminate the program.

Example :

===== Calculator =====

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Choose: 1

Enter first number: 10
Enter second number: 20

Result: 30

Then the menu should appear again.

Constraints:
-Use a while loop.
-Invalid menu options should not terminate the program.
-Division by zero must be handled.
-Option 5 should terminate the application.

Edge Cases:

Test:
0
6
-1
5
division by zero

Hints : 
Think of the program as:

START
  ↓
DISPLAY MENU
  ↓
GET OPTION
  ↓
VALIDATE OPTION
  ↓
PERFORM OPERATION
  ↓
RETURN TO MENU
  ↓
EXIT?
  ↓
YES → END
NO  → MENU
'''

# Algorithm
# Disply the menu using infinite while loop ask "choose :"
# if the input is invalid print invalid and display menu 
# Perform the arithemetic operation according to the choose
# Stop the loop when the user choose "exit"


# Initializing variables
choice = 0

while True :
    print("\n-----Calculator-----")
    print("1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n"
          "5. Exit\n"
          )
    choice = int(input("Choose :"))

    if choice == 1 :
        number_one = int(input("Enter first number:"))
        number_two = int(input("Enter second number:"))

        print(f"Sum :{number_one +number_two}\n")

    elif choice == 2 :
        number_one = int(input("Enter first number:"))
        number_two = int(input("Enter second number:"))

        print(f"Difference :{number_one - number_two}\n")

    elif choice == 3 :
        number_one = int(input("Enter first number:"))
        number_two = int(input("Enter second number:"))

        print(f"Multiplication :{number_one * number_two}\n")

    elif choice == 4 :
        number_one = int(input("Enter first number:"))
        number_two = int(input("Enter second number:"))


        if number_two ==0:
            print("Division by zero is invalid, Please re-enter the numbers")

        else :
            print(f"Division :{number_one / number_two}\n")

    elif choice == 5 :
        break

    else : 
        print("\n --- Invalid Choise --- ")