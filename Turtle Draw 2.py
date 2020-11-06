import turtle
from turtle import Turtle, Screen

screen = Screen()
t = Turtle("turtle")
t.speed(-1)                 # Max speed for the turtle

# Drag the turtle
def dragging(x, y):         # (x, y) => mouse position
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)      # Continue to call dragging function when dragging

# Clear the screen on right mouse button click
def clickright(x, y):
    t.clear()

def main():
    turtle.listen()
    t.ondrag(dragging)
    turtle.onscreenclick(clickright, 3)
    screen.mainloop()

main()
