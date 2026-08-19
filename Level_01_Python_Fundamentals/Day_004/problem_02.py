'''
Problem : Ask the user for a positive integer n.
          Calculate the sum of all integers from 1 through n.

Example :

Input:5

Output:

Sum: 15

Because:
1 + 2 + 3 + 4 + 5 = 15

Constraints:
-n > 0

Edge Cases:
-n = 1
-n = 0
-Negative input

Hints: 
You need two variables:
-counter
-total

'''

# Algorithm
# 1.Read integer value from the user
# 2.Validate the user input ( Zero and Negative numbers are not allowed)
# 3.Initialize variables, count = 1 and total_sum = 0
# 4.Use while loop with the condition (count <= user_input) 
# 5.From 1 to N calculate the sum using total_sum variable 
# 6.Stops when the loop condition false
# 7.And print the total_sum calculated 


# Initializing variables
total_sum = 0
count = 1

# Reading user input
user_input = int(input('Enter an integer value :'))

# Validating user input
while True :
    if user_input <= 0 :
        print("Invalid Input, Try again")
        user_input = int(input('Enter an integer value :'))
    else :
        break

# Calculating sum using while loop
while count <= user_input :
    total_sum += count
    count+=1 

print(f"Total sum:{total_sum}")



