'''
Problem :

Stored credentials:
- Username : admin
- Password : python123

Read username and password from the user.

Print:

Login Successful

or

Invalid Username

or

Invalid Password

Constraints:
-Username is case-sensitive.
-Password is case-sensitive.

Edge Cases:
-Empty input
-Wrong username
-Wrong password

'''

# Stored Username and Password
username = "admin"
password = "python123"

# Reading user input
input_username = input("Enter Username:").strip()
input_password = input("Enter Password:").strip()

while True :

    if input_username != username :
        print("Invalid Username , Please try again")
        input_username = input("Enter Username:").strip()
        input_password = input("Enter Password:").strip()

    elif input_password != password :
        print(f"Invalid Password , Please enter corret password {input_username}")
        input_password = input("Enter Password:").strip()

    else :
        print("Login Successful")
        break
        

