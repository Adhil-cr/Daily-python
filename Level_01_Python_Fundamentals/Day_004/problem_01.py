'''
Problem : Ask the user for a positive integer n.
          Print every number from 1 through n.

Example :

Input: 5

Output:
1
2
3
4
5

Constraints: 
- n must be greater than 0.

Edge Cases:
-1
-0
-Negative number

Hints:
-Use a while loop.
-Maintain a counter.
-Increment the counter after every iteration.
'''

# Algorithm
# 1. Read integer values from the user 
# 2. Validate the user input (Zero and Negative numbers are not allowed)
# 3. Use while loop with the condition (<= input value) 
# 4. From 1 to N prints integers using a counter variable 
# 5. The loop terminates when count <= user_input becomes False.

# Counter variable for print from 1 to N
count = 1

# Reading and validating user input
user_input = int(input("Enter an integer value: "))

while True :

    if user_input <= 0 :
        print("Invalid Input, Try again.")
        user_input = int(input("Enter an integer value: "))
    else :
        break

while count <= user_input :
    print(count)
    count +=1

