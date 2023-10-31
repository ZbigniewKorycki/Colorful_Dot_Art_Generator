import colorgram
from turtle import Turtle, Screen, colormode
import random

colors = colorgram.extract("image.jpg", 20)

first_color = colors[0]
rgb = first_color.rgb

new_colors = []
for color in colors:
    rgb = color.rgb
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    top = (red, green, blue)
    new_colors.append(top)


def color(colors):
    colour = random.choice(colors)
    return colour


screen = Screen()
timmy = Turtle()
timmy.hideturtle()
timmy.speed("fastest")
screen.setup(width=700, height=700)

colormode(255)

position_x = -325
position_y = -325

timmy.penup()
timmy.setposition(position_x, position_y)
for y in range(10):
    for x in range(10):
        random_color = color(new_colors)
        timmy.dot(20, random_color)
        timmy.forward(70)
    position_y += 70
    timmy.setposition(position_x, position_y)

screen.exitonclick()
