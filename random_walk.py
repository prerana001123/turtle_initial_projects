from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.speed("fastest")
timmy.shape("turtle")
timmy.pensize(10)


move = [0, 90, 270, 180]
colours = ["olive drab", "goldenrod", "orchid", "dark orange",
           "firebrick", "dark cyan", "medium slate blue",
           "dark goldenrod", "magenta", "rosy brown"]

for _ in range(200):
    timmy.color(random.choice(colours))
    timmy.setheading(random.choice(move))
    timmy.forward(40)


screen = Screen()
screen.exitonclick()



# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_colour = (r, g, b)
#     return random_colour