from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
E = 0
N = 90
W = 180
S = 270


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(1, 3)
        self.color(random.choice(COLORS))
        self.setpos(320,random.randint(-250,250))
        self.setheading(W)

    def move(self, speed):
        self.forward(speed)





