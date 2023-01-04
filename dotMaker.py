import random
import turtle
from turtle import *
import colorgram

timmy = Turtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(180)
timmy.forward(100)
timmy.setheading(0)
turtle.colormode(255)

colors = colorgram.extract("image.jpg", 40)
print(len(colors))


def reset_heading_position():
    timmy.setheading(90)
    timmy.forward(30)
    timmy.setheading(180)
    timmy.forward(30 * 30)
    timmy.setheading(0)


def make_dots():
    for k in range(0, 30):
        timmy.pendown()
        m = random.randint(0, len(colors) -1)
        timmy.pencolor(colors[m].rgb.r, colors[m].rgb.g, colors[m].rgb.r)
        timmy.dot(20)
        timmy.penup()
        timmy.forward(30)


for j in range(13):
    make_dots()
    reset_heading_position()

timmy.dot(25)

screen = Screen()
screen.exitonclick()
