"""
Problem

Read a word and determine whether it contains the letter: a

Print:

Contains 'a'

or

Does not contain 'a'

Use the membership operator (in).

Example:

Input:

Python

Output:

-Does not contain 'a'

Constraints:
-Treat uppercase and lowercase the same.

Edge Cases:
-Empty string.
-Single character.

"""

input_word = input("Enter a word: ").strip()


if input_word:
    input_word = input_word.lower()

    if "a" in input_word :
        print("Contains 'a'")

    else : 
        print("Does not contain 'a'")

else :
    print("Invalid Input")