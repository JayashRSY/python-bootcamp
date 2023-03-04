# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.forward(200)
#
# my_screen = Screen()
# my_screen.canvheight
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
my_table = PrettyTable()
my_table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
my_table.add_column("Type", ["Electric", "Water", "Fire"])
my_table.align = "l"
print(my_table)