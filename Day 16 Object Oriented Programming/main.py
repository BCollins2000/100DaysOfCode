# import turtle
# from turtle import Turtle, Screen
#
# import another_module
# print(another_module.another_variable)
#
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan3")
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable
#from prettytable.colortable import ColorTable, Themes

table = prettytable.PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
        ["Bulbasaur", "Grass"],
    ]
)
table.align = "l"

print(table)
