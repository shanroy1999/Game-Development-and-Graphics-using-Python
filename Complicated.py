import turtle

t = turtle.Turtle()
win = turtle.Screen()
t.getscreen().bgcolor("#994444")
t.speed(30)

def star(turtle,size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
        turtle.end_fill()
star(t, 360)
win.exitonclick()
