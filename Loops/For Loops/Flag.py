#File name: Flag.py
#Author: Sophia A
#Date created: May 9, 2025
#Description: Italy Flag with for loops

import turtle
square = turtle.Turtle()

square.color("#008000")
square.begin_fill()
square.goto(-75,25)
for i in range(1,3):
    square.forward(90)
    square.right(90)
    square.forward(180)
    square.right(90)
square.penup()
square.end_fill()

square.forward(180)
square.color("#ff0000")
square.begin_fill()
for i in range(1,3):
    square.forward(90)
    square.right(90)
    square.forward(180)
    square.right(90)
square.penup()
square.end_fill()

square.goto(25,-185)
square.color("Black")
square.write("Italy", font = ("Arial", 20, "Bold"))
square.penup()
