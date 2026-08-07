"""
Problem : 
-The account balance is ₹10,000.
-Ask the user for a withdrawal amount.

Rules:
-Amount must be positive.
-Amount cannot exceed the balance.
-If valid, display the remaining balance.
-Otherwise display an appropriate error message.

Example"

Input : 2500

Output :

Withdrawal Successful
Remaining Balance: ₹7500

Constraints:
-Withdrawal > 0

Edge Cases:
-0
-Negative amount
-More than balance
"""

# Account balence 
account_balence = 10000
print(f"\nThe account balance is ₹{account_balence:,}")

# Reading Withdrawal amount
withdrawal_amount = int(input("\nEnter the withdrawal amount :"))

while True :

    if withdrawal_amount <= 0 :
        
        print("\nInvalid Input, Witdrawal amount should be positive")
        withdrawal_amount = int(input("Enter the withdrawal amount :"))

    elif withdrawal_amount > account_balence:

        print("\nInvalid Input, Insufficent account balence")
        print(f"The account balance is ₹{account_balence:,}")
        withdrawal_amount = int(input("Enter the withdrawal amount :"))

    else :
        print(f"\nWithdrawal Successful \nRemaining Balance: ₹{account_balence-withdrawal_amount:,}")
        break

    


