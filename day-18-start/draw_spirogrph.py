from turtle import Turtle, Screen, colormode
import random


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tim = Turtle()
colormode(255)
tim.speed('fastest')


def draw_spirograph(size):
    for v in range(int(360/size)):
        tim.color(randomColor())
        tim.circle(100)
        tim.setheading(tim.heading() + size)
        print(tim.heading())


draw_spirograph(0.1)



screen = Screen()
screen.exitonclick()
