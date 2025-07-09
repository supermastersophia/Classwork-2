#File name: Yield.py
#Author: Sophia A
#Date created: March 28, 2025
#Description: This is a yield sign

import turtle
square = turtle.Turtle(）

square.color("Red")
square.begin_fill()
square.forward(200)
square.right(120)
square.forward(200)
square.right(120)
square.forward(200)
square.end_fill()

square.goto(40,-25)
square.color("White")
square.right(120)
square.begin_fill()
square.forward(125)
square.right(120)
square.forward(125)
square.right(120)
square.forward(125)
square.end_fill()

square.goto(55,-50)
square.color("Red")
square.write("YIELD", font=("Arial", 24, "Bold"))
