import turtle
win = turtle.Screen()
win.bgcolor("green")
a = turtle.Turtle()
a.color("red")
#Creating rectangle
a.left(90)
a.forward(150)
a.left(90)
a.forward(50)
a.left(90)
a.forward(150)
a.left(90)
a.forward(50)

#Creating Square
b = turtle.Turtle()
b.color("blue")
b.pensize(2)
b.forward(100)
b.right(90)
b.forward(100)
b.right(90)
b.forward(100)
b.right(90)
b.forward(100)
b.right(90)

k=turtle.Turtle()
for i in [0,1,2,3]:
    k.forward(20)
    k.left(90)

p=turtle.Turtle()
for col in ["red","blue","purple","yellow"]:
    p.color(col)
    p.forward(50)
    p.left(90)

#Creating Circle
c = turtle.Turtle()
c.color("orange")
c.pensize(3)
c.begin_fill()
c.circle(100)
c.end_fill()

#Creating Equilateral Triangle
d = turtle.Turtle()
d.color("magenta")
d.pensize(4)
d.left(120)
d.forward(100)
d.left(120)
d.forward(100)
d.left(120)
d.forward(100)

#Creating a Star
e = turtle.Turtle()
e.color("white")
e.pensize(5)
e.speed(10)
for i in range(38):
    e.forward(300)
    e.left(170)

#Creating Spiral
f = turtle.Turtle()
f.color("red")
f.pensize(4)
dist = 50
angle = 90
for i in range(17):
    f.forward(dist)
    f.right(angle)
    dist=dist+10
    angle=angle-3
win.exitonclick()
