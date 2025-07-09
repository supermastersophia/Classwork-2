# Guess the random number 

import random

number = random.randint(1,100)
print("This machine will think of a number...")
print(" ")
print(" ")

guess = (int)(input("Guess any number between 1-100: "))
print(" ")

while guess != number:
    if guess > number:
        print("Your guess is too high")
        print(" ")
    elif guess < number:
        print("The number is too low")
        print(" ")
    print(" ")
    guess = (int)(input("Guess again: "))
    print(" ")
    if guess == number:
        print("You are correct!")
        break
