# File name: Alphabet.py
# Author: Sophia A
# Date created: March 11, 2025
# Description: Checks if the letter is a vowel or consanant.

letter = input("Enter a random letter: ")
print(" ")

vowels = ["a", "e", "i", "o", "u"]
if letter.lower() in vowels:
    print("The letter is a vowel")
else:
    print("The letter is a consanant")
