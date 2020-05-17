import time
import turtle
from turtle import Turtle
from random import randint

window = turtle.Screen()
window.title("Turtle Race")         #Window Title
turtle.bgcolor("forestgreen")    #Background color
turtle.color("white")            #Text Color
turtle.speed(0)                 #Initial speed = 0
turtle.penup()                  #Pull pen up - no drawing when moving
turtle.setpos(-140, 200)        # Set Position - x axis = -140, y axis = 200
turtle.write("TURTLE RACE", font=("Arial",30,"bold"))
turtle.penup()
time.sleep(1)

turtle.setpos(-400, -180)
turtle.color("Chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()
time.sleep(1)

stamp_size = 20
square_size = 15
finish_line = 200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size/stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line, (150-(i*square_size*2)))
    turtle.stamp()

for j in range(10):
    turtle.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
    turtle.stamp()

time.sleep(1)
turtle.hideturtle()

turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("blue")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250, 100)
turtle1.pendown()

turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("magenta")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250, 50)
turtle2.pendown()

turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("black")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250, 0)
turtle3.pendown()

turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("yellow")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250, -50)
turtle4.pendown()
time.sleep(2)

for i in range(145):
    turtle1.forward(randint(1,5))
    turtle2.forward(randint(1,5))
    turtle3.forward(randint(1,5))
    turtle4.forward(randint(1,5))

turtle.exitonclick()
