from turtle import Turtle, Screen, colormode
import random

orientation = {'east': 0, 'north': 90, 'west': 180, 'south': 270}
# colors = ['blue', 'black', 'brown', 'red', 'yellow', 'green', 'orange', 'turquoise', 'pink']

tim = Turtle()
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tam = 10
for _ in range(100):
    tim.speed('fastest')
    tim.color(random_color())
    tim.pensize(tam)
    tim.setheading(random.choice(list(orientation.values())))
    tim.forward(30)
    tam += 0.1

screen = Screen()
screen.exitonclick()
