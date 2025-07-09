#File name: Stop.py
#Author: Sophia A
#Date created: March 25, 2025
#Description: This is a stop sign

import turtle
square = turtle.Turtle()
square.color("Red")
square.begin_fill()

square.forward(75)
square.left(45)
square.forward(75)
square.left(45)
square.forward(75)
square.left(45)
square.forward(75)
square.left(45)
square.forward(75)
square.left(45)
square.forward(75)
square.left(45)
square.forward(75)
square.left(45)
square.forward(75)
square.left(45)

square.end_fill()
square.penup()
square.goto(-35,70)
square.pendown()

square.color("White")
square.penup()
square.write("STOP", font=("Arial", 40, "Bold"))
square.pendown()
