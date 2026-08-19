'''
Problem :Create a login system with the following password:
         python123
         Give the user a maximum of 3 attempts.
         If the password is correct: Login Successful
         If all three attempts are incorrect: Account Locked

Example :
Enter password: hello
Incorrect password.

Enter password: test
Incorrect password.

Enter password: python123
Login Successful

Constraints :
-Maximum 3 attempts.
-Stop immediately after a successful login.

Edge Cases :
-Correct password on first attempt.
-Correct password on third attempt.
-Three incorrect attempts.
-Empty password.

Hints :
Think about:

attempt counter
+
while loop
+
break

'''

# Algorithm
# 1.initialize counter variable 'attempt' and set into 0 , also correct_password = 'python123'
# 2.Empty inputs are also an attempt 
# 2.Using while attempts < maximum_attempts, read user input
# 3.Inside the loop use if condition
# 4.if(user_input == correct_password) -> login successfull (Reset the attempt variable)
# 5.when the loop condition ' attempt < maximum_attempt ' fail the loop stops 
# 6.Check the if the attempt reaches 3  


# Initializing variables
attempt = 0
correct_password = 'python123' 

# Reading User input and validating
while attempt < 3 :
    
    input_password = input("Enter password : ").strip()

    if input_password != correct_password :
        attempt +=1
        print("Incorrect Password \n")

    else :
        print("\n---Login Successful---")
        attempt = 0
        break

if attempt == 3: 
    print("\n---Account Locked---")