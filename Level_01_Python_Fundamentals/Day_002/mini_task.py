"""
🛠 Real-World Mini Task
Employee Salary Calculator

Create a CLI application that:

Reads:
-Employee name
-Hours worked
-Hourly wage

Calculates:
-Gross salary
-Overtime pay (if hours > 40, pay 1.5× hourly wage for overtime hours)
-Displays a formatted salary summary.

Stretch Goals :
-Reject negative hours or wages.
-Keep asking until valid input is entered.
-Format salary to two decimal places using an f-string, e.g., {gross_salary:.2f}.
"""

# Reading Employee Employee name,Hours worked, Hourly wage
employe_name = input("Enter Your Name :")

hours_worked = float(input("Enter Hours Worked :"))
# Checking the input values isn't negative
while hours_worked < 0:
    print("Hours cannot be negative.")
    hours_worked = float(input("Enter Hours Worked :"))

hourly_wage = int(input("Enter Your Hourly Wage :"))
# Checking the input values isn't negative
while hourly_wage < 0 :
    print("Hourly wage cannot be negative.")
    hourly_wage = int(input("Enter Your Hourly Wage :"))

# Calculating The Salary
if hours_worked <= 40 :
    gross_salary = hours_worked * hourly_wage

if hours_worked > 40 :
    overtime_salary = hourly_wage * 1.5
    gross_salary = 40 * hourly_wage + (hours_worked-40)*overtime_salary


# Display 
print("\nEmployee Salary Summary")
print('-----------------------')
print(f"Employe : {employe_name}\n"
      f"Hours : {hours_worked}\n"
      f"Wage : {hourly_wage}\n")
print(f"Gross Salary : {gross_salary:.2f}")
