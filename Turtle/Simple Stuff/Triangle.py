#File name: Triangle.py
#Author: Sophia A
#Date created: March 19, 2025
#Description: Drawing of a triangle

import turtle
triangle = turtle.Turtle()

triangle.color("Red")
triangle.begin_fill()
triangle.forward(100)
triangle.left(120)
triangle.forward(100)
triangle.left(120)
triangle.forward(100)

triangle.penup()
triangle.end_fill()
triangle.pendown()
