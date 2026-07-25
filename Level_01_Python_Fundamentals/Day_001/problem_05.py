"""
Problem 5 — Profile Generator

Collect:

Name
Age
City
Profession
Favorite Programming Language

Display a formatted profile.
"""

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
city = input("Enter your City: ")
profession = input("Enter your Profession: ")
programming_language = input("Enter your Favorite programming language: ")

print(f"Your name is {name} and you are {age} years old.You comming from {city} and your profession is {profession} also your favourite programming language is {programming_language}.")