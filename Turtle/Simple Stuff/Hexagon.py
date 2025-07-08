#File name: Hexagon.py
#Author: Sophia A
#Date created: March 20, 2025
#Description: Drawing of a hexagon

import turtle
hexagon = turtle.Turtle()

hexagon.pencolor("#2af3f4")
hexagon.pensize(5)
hexagon.color("#2af3f4")
hexagon.begin_fill()

hexagon.forward(100)
hexagon.left(60)
hexagon.forward(100)
hexagon.left(60)
hexagon.forward(100)
hexagon.left(60)
hexagon.forward(100)
hexagon.left(60)
hexagon.forward(100)
hexagon.left(60)

hexagon.penup()
hexagon.end_fill()
hexagon.pendown()
