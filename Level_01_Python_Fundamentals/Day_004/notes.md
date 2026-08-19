# Day 004 Notes

## 1. While Loop

A `while` loop repeatedly executes a block of code **while its condition remains `True`**.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### Output

```text
1
2
3
4
5
```

---

## 2. Loop Counter

A **counter** is a variable used to track the current iteration of a loop.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

The counter must change during each iteration so that the loop can eventually terminate.

```python
count += 1
```

Without updating the counter, the loop may become an **infinite loop**.

---

## 3. Infinite Loop

```python
while True:
    print("Running")
```

`while True` creates a loop that continues indefinitely unless something inside the loop terminates it.

An infinite loop can be intentionally used when a program needs to continue running until a specific condition occurs.

---

## 4. `break`

The `break` statement **immediately terminates the nearest enclosing loop**.

```python
while True:
    password = input("Password: ")

    if password == "python123":
        print("Login Successful")
        break
```

### How it works

1. The program repeatedly asks for the password.
2. If the password is incorrect, the loop continues.
3. If the password is correct, `break` terminates the loop.

---

## 5. `continue`

The `continue` statement **skips the remaining statements in the current iteration** and moves to the next iteration of the loop.

```python
count = 0

while count < 5:
    count += 1

    if count == 3:
        continue

    print(count)
```

### Output

```text
1
2
4
5
```

When `count` becomes `3`, `continue` skips the `print()` statement for that iteration.

---

## 6. Input Validation with `while`

A loop can repeatedly request input until a **valid value** is provided.

```python
while True:
    age = int(input("Enter age: "))

    if 0 <= age <= 120:
        break

    print("Invalid age")
```

### How it works

* The program asks the user for an age.
* The input is checked against the validation condition.
* If the age is valid, `break` exits the loop.
* If the age is invalid, an error message is displayed.
* The loop asks for the input again.

This is more reliable than asking the user to retry a fixed number of times.

> **Note:** `try/except` should be added later to handle non-numeric input such as `"abc"` without crashing the program.

---

## 7. State

**State** represents the current condition or value of something in a program.

A variable can represent changing program state.

```python
balance = 10000

balance += 500
balance -= 200
```

The value of `balance` changes as the program executes.

### Final Value

```text
10300
```

State is important in programs such as:

* Banking systems
* Shopping carts
* Games
* Login systems
* Counters
* Inventory systems

---

## 8. Accumulator Pattern

An **accumulator** is a variable that stores and continuously builds a result during loop execution.

```python
total = 0
count = 1

while count <= 5:
    total += count
    count += 1
```

### Execution

```text
total = 0
total = 0 + 1
total = 1 + 2
total = 3 + 3
total = 6 + 4
total = 10 + 5
```

### Final Result

```text
total = 15
```

The `total` variable **accumulates** the result of each iteration.

---

## 9. Counter vs Accumulator

### Counter

A counter tracks **progress or the number of iterations**.

```python
count += 1
```

Example:

```python
count = 0

while count < 5:
    count += 1
```

### Accumulator

An accumulator **builds or stores a result**.

```python
total += count
```

Example:

```python
total = 0

while count <= 5:
    total += count
```

### Simple Difference

```text
Counter     → Tracks progress
Accumulator → Builds a result
```

---

## 10. Menu-Driven Programs

A **menu-driven CLI application** commonly follows this structure:

1. Display menu.
2. Read user's choice.
3. Process the selected choice.
4. Repeat the menu.
5. Exit when the user chooses the exit option.

Example:

```python
while True:
    display_menu()

    choice = input("Choose: ")

    if choice == "4":
        break
```

This pattern is commonly used for:

* Banking applications
* To-do applications
* Inventory systems
* Student management systems
* CLI utilities

---

## 11. Algorithm Planning

Before writing code, follow a structured problem-solving process:

1. **Understand the problem**
2. **Identify inputs**
3. **Identify required processing**
4. **Identify outputs**
5. **Identify validation requirements**
6. **Identify edge cases**
7. **Write the algorithm**
8. **Implement the solution**
9. **Test the solution**
10. **Refactor and improve the code**

### Example

For a program that calculates the average of numbers:

```text
Input
  ↓
Validate input
  ↓
Process numbers
  ↓
Calculate average
  ↓
Display result
  ↓
Test edge cases
```

---

## Key Takeaways

* `while` repeats code while a condition is `True`.
* A **counter** tracks loop progress.
* `while True` creates an intentional infinite loop.
* `break` terminates the nearest loop immediately.
* `continue` skips the current iteration and starts the next one.
* Loops are useful for **input validation**.
* **State** represents changing values during program execution.
* An **accumulator** builds a result during iteration.
* Menu-driven CLI applications commonly use `while True` with `break`.
* Good programmers **plan the algorithm before implementing the code**.
