'''
Problem : Create a number guessing game.
          The secret number is: 37
          Keep asking the user to guess until they find the correct number.

For each guess:
    If the guess is too low: Too Low

    If the guess is too high: Too High

    If correct: Correct!

Also display the number of attempts when the user wins.

Example :
Enter your guess: 20
Too Low

Enter your guess: 50
Too High

Enter your guess: 37
Correct!

Attempts: 3


Constraints:
-Guess must be an integer.
-Continue until the correct answer is entered.

Edge Cases:
-Correct on first attempt.
-Repeated incorrect guesses.
-Negative guesses.

Hints:
You'll need:
    while
    if / elif / else
    counter
    break
    
'''

# Algorithm
# Initialize variables secret_number=37 and attempt=0 
# Use Infinite loop to read until the guess become correct 
# Read and validate user input isn't zero and less than
# if user_input is greater than secret_number disply " Too high" and increment attempt
# if user_input is less than secret_number disply " Too low" and increment attempt
# keep asking until the guess correct



# Initializing variables
attempt = 0
secret_number = 37

while True :
    # Reading and validating user input
    user_input = int(input("Enter your guess: "))

    if user_input <=0 :
            print("Invalid input")

    elif user_input == secret_number:
        print("Correct!")
        print(f"Attempts : {attempt+1}")
        break

    elif user_input < secret_number :
        print("Too low")
        attempt +=1

    elif user_input > secret_number :
        print("Too high")
        attempt +=1
