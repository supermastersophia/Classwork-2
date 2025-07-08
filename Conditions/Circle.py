#File name: Circle.py
#Author: Sophia A
#Date created: March 14, 2025
#Description: Area and circumference

print("Would you like to calculate the circumference or area?")
print(" ")
print("A) circumference")
print("B) area")

print(" ")
choice = (input(" "))

print(" ")
radius = (int)(input("Enter the radius (integer only): "))
pi = 3.14

if choice == 'A' or choice == 'a':
    print(" ")
    circumference = (radius*2)*pi
    print(" ")
    print(" ")
    print("The circumference is...")
    print(" ")
    print(circumference) 
elif choice == "B" or choice == 'b':
    print(" ")
    area = pi*(radius*radius)
    print(" ")
    print(" ")
    print("The area is...")
    print(" ")
    print(area)  
else:
    print(" ")
    print("ERROR")
    exit()
