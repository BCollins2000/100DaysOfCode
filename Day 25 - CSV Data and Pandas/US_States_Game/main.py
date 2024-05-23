import turtle
import csv
import pandas as pd
pd.set_option('display.max_columns', None)

states_data = pd.read_csv("50_states.csv")

#print(states_names)


screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

guess_correct = 0
while guess_correct < 50:
    answer_state = screen.textinput(title=f'Guess the state {guess_correct}/50', prompt='Whats another state name?').title()
    if answer_state == "Exit":
        break
    if answer_state in states_data["state"].values:
        answer_db = states_data[states_data["state"] == answer_state]
        state_x = int(answer_db['x'])
        state_y = int(answer_db['y'])
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.speed("fastest")
        new_turtle.penup()
        new_turtle.goto((state_x, state_y))
        new_turtle.write(answer_state, align="center")
        guess_correct += 1
        states_data = states_data[states_data["state"] != answer_state]

states_data["state"].to_csv('states_missed.csv', index = False)





#answer_state = screen.textinput(title='Guess the state', prompt='Whats another state name?')
answer_state = answer_state.title()
