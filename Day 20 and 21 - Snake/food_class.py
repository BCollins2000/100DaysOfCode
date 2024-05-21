from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.setpos(random.randint(-14,14)*20,random.randint(-14,14)*20)

    def refresh(self):
        self.setpos(random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)

