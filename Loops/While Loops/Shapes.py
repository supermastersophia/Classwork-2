# File name: Shapes.py
# Author: Sophia A
# Date created: April 11, 2025
# Description: 3 random shapes with color

import turtle

square = turtle.Turtle()

square.color("#ffffff")
square.goto(-25, 0)
square.color("#00ff00")
square.begin_fill()
i = 1
while i <= 5:
    square.forward(70)
    square.left(72)
    i = i + 1
square.penup()
square.end_fill()

square.goto(-160, 0)
square.color("#ff0000")
square.begin_fill()
i = 1
while i <= 3:
    square.forward(105)
    square.left(120)
    i = i + 1
square.penup()
square.end_fill()

square.goto(110, 0)
square.color("#00afff")
square.begin_fill()
i = 1
while i <= 6:
    square.forward(60)
    square.left(60)
    i = i + 1
square.penup()
square.end_fill()

square.goto(-27, -25)
square.color("Black")
square.write("pentagon", font=("Arial", 12, "Bold"))
square.penup()

square.goto(-140, -25)
square.write("triangle", font=("Arial", 12, "Bold"))
square.penup()

square.goto(110, -25)
square.write("hexagon", font=("Arial", 12, "Bold"))
square.penup()
square.pendown()
