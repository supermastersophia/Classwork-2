# File name: Stop.py
# Author: Sophia A
# Date created: March 25, 2025
# Description: Drawing of a STOP sign

import turtle

sign = turtle.Turtle()
sign.color("Red")
sign.begin_fill()

sign.forward(75)
sign.left(45)
sign.forward(75)
sign.left(45)
sign.forward(75)
sign.left(45)
sign.forward(75)
sign.left(45)
sign.forward(75)
sign.left(45)
sign.forward(75)
sign.left(45)
sign.forward(75)
sign.left(45)
sign.forward(75)
sign.left(45)

sign.end_fill()
sign.penup()
sign.goto(-35,70)
sign.pendown()

sign.color("White")
sign.penup()
sign.write("STOP", font=("Arial", 40, "Bold"))
sign.pendown()
