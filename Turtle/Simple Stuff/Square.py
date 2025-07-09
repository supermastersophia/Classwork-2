# File name: Square.py
# Author: Sophia A
# Date created: March 19, 2025
# Description: This is a square

import turtle

square = turtle.Turtle()

square.pencolor("Orange")
square.pensize(5)
square.color("Orange")
square.begin_fill()

square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)

square.penup()
square.end_fill()
square.pendown()
