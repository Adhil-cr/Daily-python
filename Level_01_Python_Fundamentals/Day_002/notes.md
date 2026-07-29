# Day 002 Notes

# Operators

An operator is a symbol that performs an operation on one or more operands.

Example:

```python
10 + 5
```

Here:

- 10 and 5 are operands.
- + is the operator.

---

# 1. Arithmetic Operators

Used to perform mathematical calculations.

| Operator | Description    |
| -------- | -------------- |
| +        | Addition       |
| -        | Subtraction    |
| *        | Multiplication |
| /        | Division       |
| //       | Floor Division |
| %        | Modulus        |
| **       | Exponent       |

Examples:

```python
10 + 5
10 - 5
10 * 5
10 / 5
10 // 3
10 % 3
2 ** 4
```

Important:

- `/` always returns a float.
- `//` returns the integer quotient.
- `%` returns the remainder.

Real-world use:

- Shopping carts
- Salary calculations
- Even/Odd checking
- Pagination
- Time calculations

---

# 2. Comparison Operators

Comparison operators compare two values and always return a Boolean (`True` or `False`).

| Operator | Meaning               |
| -------- | --------------------- |
| ==       | Equal                 |
| !=       | Not Equal             |
| >        | Greater Than          |
| <        | Less Than             |
| >=       | Greater Than or Equal |
| <=       | Less Than or Equal    |

Example:

```python
18 >= 18
```

Returns:

```python
True
```

---

# 3. Logical Operators

Used to combine multiple conditions.

## and

Returns `True` only if all conditions are `True`.

Example:

```python
age > 18 and age < 60
```

---

## or

Returns `True` if at least one condition is `True`.

Example:

```python
marks >= 40 or sports_quota
```

---

## not

Reverses the Boolean value.

Example:

```python
not True
```

Returns:

```python
False
```

---

# 4. Assignment Operators

Used to assign or update variable values.

```python
count = 10
count += 5
count -= 2
count *= 3
count /= 2
count //= 2
count %= 3
```

These make code shorter and easier to read.

---

# 5. Membership Operators

Used to check whether a value exists inside a sequence.

Operators:

- in
- not in

Example:

```python
"Py" in "Python"
```

Returns:

```python
True
```

---

# 6. Operator Precedence

Python evaluates expressions in this order:

1. Parentheses `()`
2. Exponent `**`
3. Multiplication, Division, Floor Division, Modulus
4. Addition and Subtraction
5. Comparison Operators
6. not
7. and
8. or

Example:

```python
2 + 3 * 4
```

Result:

```python
14
```

Example:

```python
(2 + 3) * 4
```

Result:

```python
20
```

---

# Best Practices

- Use meaningful variable names.
- Use parentheses to improve readability.
- Never use `=` when comparing values.
- Avoid using Python built-in function names as variable names (`sum`, `list`, `str`, etc.).
- Validate user input whenever possible.

---

# Common Mistakes

❌ Using `=` instead of `==`

❌ Dividing by zero

❌ Forgetting operator precedence

❌ Using `%` without understanding remainders

❌ Shadowing built-in function names

---

# Key Takeaways

- Operators are used to perform operations on values.
- Comparison operators always return a Boolean.
- Logical operators combine conditions.
- `%` is useful for checking even/odd numbers.
- `//` returns the floor division result.
- Parentheses improve readability and avoid precedence mistakes.
