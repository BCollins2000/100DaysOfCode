import time
from turtle import Screen
from player import Player

from car_manager import Car
from scoreboard import Scoreboard, GoalLine
import random

goal_y = 260


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

level = Scoreboard((150, goal_y+10),"Level Number")
level.score_count = 1
level.refresh_score()

num_cars = Scoreboard((-150, goal_y+10),"Number of Cars")

frog = Player()
goal = GoalLine(goal_y)

screen.listen()
screen.onkey(frog.go_up,"Up")
screen.onkey(frog.go_down,"Down")
screen.onkey(frog.go_left,"Left")
screen.onkey(frog.go_right,"Right")

car_list = []
car_probability = .05
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    num_cars.score_count = len(car_list)
    num_cars.refresh_score()
    car_gen = random.random()
    if car_gen < car_probability:
        new_car = Car()
        car_list.append(new_car)
    for car in car_list:
        car.move(5+level.score_count)
        if abs(frog.xcor() - car.xcor()) < 30 and abs(frog.ycor() - car.ycor()) < 10:
            level.game_over()
            game_is_on = False
    if frog.ycor() > goal_y:
        frog.reset_turtle()
        level.increase_score()
        car_probability += .03
    car_list = [car for car in car_list if car.xcor() >= -330]

screen.exitonclick()