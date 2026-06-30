import random
import turtle
from turtle import Turtle, Screen
tim = Turtle(shape="turtle")
turtle.colormode(255)
tim.speed(0)
# tim.pensize(2)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading( tim.heading() + size_of_gap)


draw_spirograph(5)
screen = Screen()
screen.exitonclick()

