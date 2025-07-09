#File name: Sum.py
#Author: Sophia
#Date created: April 15, 2025
#Description: Sum of random numbers

number = (int)(input("Enter a number: "))
total = 0

i = 2
while i <= number:
    total = total + i
    i = i + 2

print(" ")
print(" ")
print("The sum of the Even #s is... ", total)
