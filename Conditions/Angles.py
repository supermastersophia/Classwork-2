# File name: Angles.py
# Author: Sophia A
# Date created: March 11, 2025
# Description: Classifies angles

angle = (int)(input("Enter a number between 0 and 360: "))
print(" ")

if (angle < 0) or (angle > 360):
    print(" ")
    print("The angle should be between 0 and 360")
elif angle < 90:
    print(" ")
    print("This is an acute angle")
elif angle == 90:
    print(" ")
    print("This is an right angle")
elif (angle > 90) and (angle < 180):
    print(" ")
    print("This is a obtuse angle")
elif angle == 180:
    print(" ")
    print("This is a straight angle")
elif (angle > 180) and (angle < 360):
    print(" ")
    print("This is a reflex angle")
else:
    exit()
