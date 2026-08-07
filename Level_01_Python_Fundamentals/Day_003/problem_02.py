"""

Problem: Read marks (0–100).

Display:

A
B
C
D
F

Grade Rules:
90–100 → A
75–89  → B
60–74  → C
40–59  → D
Below 40 → F

Constraints:
-Marks must be between 0 and 100.

Edge Cases:
-0
-100
-Invalid marks

Hints:
-Use an if-elif-else ladder.
-Check invalid input first.
"""

# Reading user input
mark = int(input("Enter your mark(0-100):"))

# Validating the input
while True :
    if mark<0 or mark>100 :
        print("invalid input,Please enter your mark(0-100):")
        mark = int(input("Enter your mark(0-100):"))
    else :
        break

# Display Grade
if mark >= 90:
    print("A")

elif mark >= 75:
    print("B")

elif mark >= 60:
    print("C")

elif mark >= 40:
    print("D")
    
else:
    print("F")