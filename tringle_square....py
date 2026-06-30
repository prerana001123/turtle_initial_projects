import random
from turtle import Turtle, Screen
tom = Turtle()
tom.shape("turtle")
colors = ["olive drab", "goldenrod", "orchid", "dark orange",
          "firebrick", "dark cyan", "medium slate blue",
          "dark goldenrod", "magenta", "rosy brown"]


def shapes(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tom.pensize(2)
        tom.forward(100)
        tom.right(angle)
        tom.shapesize(2)


for sides in range(3, 11):
    tom.color(random.choice(colors))
    shapes(sides)
screen = Screen()
screen.exitonclick()
