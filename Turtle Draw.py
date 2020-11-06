import turtle
import random
from turtle import *

t = turtle.Turtle()
t.speed(0)
t.width(5)

colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

# Defining functions to see what happens when a certain key is pressed
def up():
    t.setheading(90)
    t.forward(100)

def down():
    t.setheading(270)
    t.forward(100)

def left():
    t.setheading(180)
    t.forward(100)

def right():
    t.setheading(0)
    t.forward(100)

# Change color when click left mouse button
def clickLeft(x, y):
    t.color(random.choice(colors))

# Stamp the turtle down on screen when click right mouse button
def clickRight(x, y):
    t.stamp()

turtle.listen()

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

# 1 => left mouse button, 2 => middle mouse button, 3 => right mouse button
turtle.onscreenclick(clickLeft, 1)
turtle.onscreenclick(clickRight, 3)

# Keep continuing to look for key presses until we close the window
turtle.mainloop()
