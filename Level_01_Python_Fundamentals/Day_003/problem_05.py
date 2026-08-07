'''
Problem: Calculate the electricity bill using the following rules:

Units	Rate
0–100	₹5/unit
101–200	₹7/unit
Above 200	₹10/unit

Assume the entire bill is charged using the rate 
for the slab the total usage falls into (no progressive slabs yet).

Example :

Input :150

Output :

-Bill Amount: ₹1050

Constraints :
-Units must be non-negative.

Edge Cases :
-0
-100
-101
-200
-201

'''

# Reading user input , Total units used
unit = int(input('Enter the Unit: '))

if unit < 0 :
    print("Invalid input")

else :
    if unit <= 100 :
        total_bill = unit * 5
        print(f"Bill Amount : {total_bill}")

    elif unit <= 200 :
        total_bill = unit * 7
        print(f"Bill Amount : {total_bill}")
        
    else :
        total_bill = unit * 10
        print(f"Bill Amount : {total_bill}")