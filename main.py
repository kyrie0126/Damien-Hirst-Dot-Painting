import turtle
import colorgram
from turtle import Turtle, Screen
from random import choice


# Create color palette from image
colors = colorgram.extract('damien-hirst.jpg', 30)
rgb_palette = []
for i in range(0, 30):
    col = tuple(colors[i].rgb)
    rgb_palette.append(col)


# Create painting
tim = Turtle()
tim.penup()
for i in range(1, 11):
    tim.goto(-250, -250 + 50 * i)
    for i in range(1, 11):
        random_color = choice(rgb_palette)
        turtle.colormode(255)
        tim.dot(20, random_color)
        tim.forward(50)


# Print screen
screen = Screen()
screen.exitonclick()
print(screen)