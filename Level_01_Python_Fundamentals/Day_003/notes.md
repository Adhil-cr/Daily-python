# Day 003 Notes

# Conditional Statements

Conditional statements allow a program to make decisions based on conditions.

---

# if Statement

Executes a block only when the condition is True.

```python
age = 20

if age >= 18:
    print("Adult")
```

---

# if-else Statement

Provides two possible execution paths.

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

# if-elif-else Statement

Used when multiple conditions need to be checked.

```python
marks = 82

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")
```

Python stops checking once it finds the first True condition.

---

# Nested if

An if statement inside another if statement.

```python
if age >= 18:
    if has_license:
        print("Can Drive")
```

Use nesting only when it improves readability.

---

# Boolean Expressions

Comparison operators return Boolean values.

Examples:

```python
age >= 18
marks < 40
```

Logical operators:

- and
- or
- not

---

# Input Validation

Always validate user input before processing it.

```python
if age < 0 or age > 120:
    print("Invalid Age")
```

---

# Best Practices

- Validate input first.
- Keep conditions simple.
- Match problem requirements exactly.
- Use meaningful variable names.
- Avoid unnecessary nesting.

---

# Common Mistakes

- Using = instead of ==
- Incorrect indentation
- Wrong condition order
- Ignoring edge cases
- Forgetting boundary values

---

# Key Takeaways

- if executes code when a condition is True.
- else handles the alternative case.
- elif checks multiple conditions.
- Nested if handles dependent conditions.
- Input validation improves program reliability.