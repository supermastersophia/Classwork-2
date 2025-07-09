#File name: Pentagon.py
#Author: Sophia A
#Date created: March 19, 2025
#Description: This is a pentagon

import turtle
pentagon = turtle.Turtle()

pentagon.pencolor("#12ff0b")
pentagon.pensize(5)
pentagon.color("#12ff0b")
pentagon.begin_fill()

pentagon.forward(100)
pentagon.left(72)
pentagon.forward(100)
pentagon.left(72)
pentagon.forward(100)
pentagon.left(72)
pentagon.forward(100)
pentagon.left(72)
pentagon.forward(100)
pentagon.left(72)

pentagon.penup()
pentagon.end_fill()
pentagon.pendown()
