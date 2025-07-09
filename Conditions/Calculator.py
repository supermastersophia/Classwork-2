# File name: Calculator.py
# Author: Sophia A
# Date created: March 14, 2025
# Description: This is a calculator

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponent (Cube)")
print("6. Square root")
print("7. Exit")
print(" ")

choice = int(input("Enter your choice: "))
if choice >= 1 and choice <= 4:
    print(" ")
    print("Enter two numbers: ")
    print(" ")

    num1 = int(input())
    print(" ")
    num2 = int(input())

    if choice == 1:
        res = num1 + num2
    elif choice == 2:
        res = num1 - num2
    elif choice == 3:
        res = num1 * num2
    elif choice == 4:
        res = num1 / num2

elif choice == 5:
    print(" ")
    print("Enter a number: ")
    num1 = int(input())
    res = num1 * num1 * num1
elif choice == 6:
    print(" ")
    print("Enter a number: ")
    num1 = int(input())
    res = num1**0.5
elif choice == 7:
    exit()

print(" ")
print("Result =", res)
