import turtle
from turtle import Turtle, Screen
import colorgram
import random

tim = Turtle()
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
turtle.colormode(255)
rgb_colors = [(240, 239, 236), (233, 237, 244), (243, 234, 240), (238, 245, 241), (204, 157, 108), (160, 84, 40), (7, 20, 58), (148, 8, 48), (234, 214, 93), (31, 100, 153), (68, 7, 37), (131, 168, 194), (52, 18, 12), (195, 144, 168), (192, 160, 29), (146, 65, 98), (19, 56, 126), (142, 173, 156), (12, 46, 30), (135, 32, 21)]

tim.hideturtle()
tim.penup()
tim.right(90)
tim.forward(250)
tim.right(90)
tim.forward(250)
tim.right(180)
tim.pendown()

for _ in range(11):
    for _ in range(11):
        tim.dot(20, random.choice(rgb_colors))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(550)
    tim.left(180)
    tim.pendown()



screen = Screen()
screen.exitonclick()