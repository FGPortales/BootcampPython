from turtle import Turtle, Screen
import random

tim = Turtle()
sides = 3

colors = ['blue', 'black', 'brown', 'red', 'yellow', 'green', 'orange', 'turquoise', 'pink']

for _ in range(7):
    size = 100
    angle = 360/sides
    tim.color(random.choice(colors))
    for s in range(sides):
        tim.right(angle)
        tim.forward(size)
    sides += 1

screen = Screen()
screen.exitonclick()
