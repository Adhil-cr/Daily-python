'''
Interactive ATM Simulator : This is your first mini task where 
                            several concepts come together.

Create a CLI ATM application with an initial balance of: ₹10,000

Display a menu:

====== ATM ======


1. Check Balance
2. Deposit
3. Withdraw
4. Exit

The application should continue running until the user chooses 4.

Features
1. Check Balance

Display:
Current Balance: ₹10,000.00

2. Deposit
Ask for an amount.
Rules:
-Amount must be greater than 0.
-Add it to the balance.

3. Withdraw
Ask for an amount.
Rules:
-Amount must be greater than 0.
-Amount cannot exceed the current balance.
-Deduct it from the balance.

4. Exit
Display:Thank you for using the ATM.

and terminate.
'''

# Algorithm
# Initialize variable account_balence = 10,000.
# Using infinte loop run the program continuesly.
# Display the choices.
# validate the entered choice and perform corresponding task.
# always update the account_balence according to the task perform


# Initialize variables
account_balance = 10000
choice = 0

# Infinite loop
while True :
    print("\n====== ATM ======")
    print("1. Check Balance\n"
          "2. Deposit\n"
          "3. Withdraw\n"
          "4. Exit\n"
          )
    choice = int(input("\nChoose : "))

    # Check balence
    if choice == 1 :
        print(f"\nCurrent Balance:₹{float(account_balance):,}")

    # Deposit amount
    elif choice == 2 :
        deposit_amount = int(input("Enter the deposit amount: "))

        while True :
            if deposit_amount <=0 :
                print("Invalid Input,Enter a valid amount")
                deposit_amount = int(input("Enter the deposit amount: "))
            else :
                account_balance = account_balance + deposit_amount
                print(f"\nCurrent Balance:₹{float(account_balance):,}")
                break


    # Withdraw amount
    elif choice == 3 :
        withdraw_amount = int(input("Enter the withdrawal amount: "))

        while True:
            if withdraw_amount > account_balance or withdraw_amount <=0:
                print("Invalid Input , Try again")
                withdraw_amount = int(input("Enter the withdrawal amount: "))

            else :
                account_balance = account_balance - withdraw_amount
                print(f"\nCurrent Balance:₹{float(account_balance):,}")
                break

    # Exit the program
    elif choice == 4 :
        print("------ Thank you for using the ATM ------")
        break

    else :
        print("Invalid Input")