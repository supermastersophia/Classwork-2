# File name: Age.py
# Author: Sophia A
# Date created: Feburary 4, 2025
# Description: This is my age in weeks

question = int(input("Enter your current age: "))
print(" ")
print("This is your age in weeks:")

age = (question * 365) + (question // 4)
int(age)
weeks = age // 7
int(weeks)
final_age = (age % 7) + weeks

print(final_age)
