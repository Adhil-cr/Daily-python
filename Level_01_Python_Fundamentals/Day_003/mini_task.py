'''
Mini Task — Smart BMI Calculator 

Build a CLI application that:

Collect:
-Name
-Age
-Height (meters)
-Weight (kg)

Calculate BMI:
-BMI = weight / (height²)

Display:
    BMI	Category :
    <18.5	    Underweight
    18.5–24.9	Normal
    25–29.9	    Overweight
    ≥30	        bese

Requirements:
-Validate all inputs.
-Reject invalid height or weight.
-Format BMI to 2 decimal places.
-Display a clean summary.

'''

# Reading and validating Name
name = input("\nEnter your name:").strip()
while True:
    if name:
        print(name)
        break
    else :
        print("\nInvalid Input, Try again")
        name = input("\nEnter your name:").strip()


# Reading and validating Age
age = int(input("\nEnter your age: "))

while True:
    if age > 0 and age <=120 :
        print(f"Valid age {age}")
        break
    else :
        print("\nInvalid Age, Try again")
        age = int(input("\nEnter your age: "))

# Reading and validating user height 
height = float(input("\nEnter your height(In Meters):")) 

while True :
    # Validating the height is not empty and invalid  
    if height :
        if height < 0.5 or height > 2.5 :
            print("Invalid height, Please enter a valid height")
            height = float(input("\nEnter your height(In Meters):")) 
        else :
            print(f"Valid height {height}")
            break

    else :
        print("Invalid Input, Height can't be empty")
        height = float(input("\nEnter your height(In Meters):"))


# Reading and validating user Weight
weight = float(input("Enter your weight(In Kg):"))

while True:
    if weight :
        if weight <2 or weight >500:
            print("Invalid Weight , Please enter a valid Weight(0-500kg) :")
            weight = float(input("Enter your weight(In Kg):"))

        else:
            print(f"Valid Weight:{weight}")
            break

    else :
        print("Invalid Input, Weight can't be empty")
        weight = float(input("Enter your weight(In Kg):"))



BMI = weight / (height*height)


# Displaying summary
print()
print('======== BMI SUMMARY ========')
print(f"Name : {name}")
print(f"Age : {age} years")
print(f"Height : {height} M")
print(f"Weight : {weight} KG")
print(f"BMI : {BMI :.2f}")


if BMI < 18.5 :
    print("Category : Under Weight")
elif BMI <= 24.9 :
    print("Category : Normal Weight")
elif BMI <= 29.0 :
    print("Category : Over Weight")
else :
    print("Category : Obese")

print('=============================')