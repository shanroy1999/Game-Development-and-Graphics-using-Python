import turtle
win = turtle.Screen()
win.bgcolor("lightgreen")
t = turtle.Turtle()
t.color("blue")
t.shape("turtle")
dist = 5
t.up()
for i in range(30):
    t.stamp()
    t.forward(dist)
    t.right(24)
    dist = dist+2
win.exitonclick()
