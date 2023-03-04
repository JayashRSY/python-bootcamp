import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win?(Red, Green, Blue, Yellow, Purple): ")
colors = ["red", "green", "blue", "yellow", "purple"]
y_position = [80, 40, 0, -40, -80]

all_turtles = []
for turtle_index in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:
    for tur in all_turtles:
        if tur.xcor() > 230:
            is_race_on = False
            winning_color = tur.pencolor()
            if winning_color == user_bet:
                print(f"You Won!  {winning_color} Turtle Won the Race")
            else:
                print(f"You Lost!  {winning_color} Turtle Won the Race")

        rand_distance = random.randint(0, 10)
        tur.forward(rand_distance)


screen.exitonclick()