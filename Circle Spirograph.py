import turtle
import time
win = turtle.Screen()
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(6):
    for colors in ["red","blue","magenta","cyan","green","yellow","white"]:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()
win.exitonclick()
