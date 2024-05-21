from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make your bet!', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_list = [-100, -60, -20, 20, 60, 100]
turtle_list = []

for i in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.speed('fastest')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.setx(-230)
    new_turtle.sety(y_list[i])
    turtle_list.append(new_turtle)

race_on = True
while race_on:
    x_locations = []
    for t in turtle_list:
        x_locations.append(t.xcor())
    if max(x_locations) < 230:
        for t in turtle_list:
            t.forward(random.uniform(0,50))
    else:
        max_value = max(x_locations)
        max_index = x_locations.index(max_value)
        winning_color = turtle_list[max_index].color()[1]
        race_on = False

if user_bet.lower() == winning_color:
    print(f'Good Job! The winning color was {winning_color}')
else:
    print(f'Sorry! The winning color was {winning_color}')

screen.exitonclick()