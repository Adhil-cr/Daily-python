"""
Problem 4 — Temperature Converter

Input Celsius.

Output:

Fahrenheit:
Kelvin:

Use the correct formulas.
"""

celsius = int(input("Enter the Temperature(In celsius): "))
fahrenheit = (celsius*1.8) + 32
kelvin = celsius + 273.15

print(f"Celsius:{celsius}°C , Faranheit:{fahrenheit}°F, Kelvin:{kelvin}k")