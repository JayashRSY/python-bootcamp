import turtle
from turtle import Turtle, Screen
#for changing color mode in random color generator
turtle.colormode(255)
import random

tim = Turtle()
#################################
# # SHAPE ND COLOR
# tim.shape("turtle")
# tim.color("red", "green")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# tim.right(180)
# # DOTTED LINE
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
######################################################
# SHAPES WITH DIFFERENT COLOR
# color_list = ["blue", "sky blue", "cyan", "dark cyan", "sea green", "lime", "yellow", "goldenrod", "sienna", "moccasin", "orange", "firebrick", "maroon", "orange red", "deep pink", "medium violet red", "magenta", "dark violet", "indigo"]
# def draw_shape(num_of_side):
#     angle = 360 / num_of_side
#     for _ in range(num_of_side):
#         tim.forward(100)
#         tim.left(angle)
#
# for i in range(3, 10):
#     tim.color(random.choice(color_list))
#     draw_shape(i)
#######################################################
# GENERATE RANDOM COLOR PATH
#color_list = ["blue", "sky blue", "cyan", "dark cyan", "sea green", "lime", "yellow", "goldenrod", "sienna", "moccasin", "orange", "firebrick", "maroon", "orange red", "deep pink", "medium violet red", "magenta", "dark violet", "indigo"]
#Random color without colorlist
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# path_dir = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed("fastest")
# for _ in range(100):
#     # tim.color(random.choice(color_list))
#     tim.color(random_color())
#     tim.setheading(random.choice(path_dir))
#     tim.forward(30)
##########################################################################
# SPINOGRAPH
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
tim.speed("fastest")

def draw_spinograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
draw_spinograph(5)
###############################################################################




# SCREEN
screen = Screen()
screen.exitonclick()
