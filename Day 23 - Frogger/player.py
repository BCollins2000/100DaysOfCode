from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
E = 0
N = 90
W = 180
S = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('green')
        self.setheading(N)
        self.setpos(STARTING_POSITION)

    def reset_turtle(self):
        self.setpos(STARTING_POSITION)

    def go_up(self):
        self.setheading(N)
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.setheading(S)
        self.forward(MOVE_DISTANCE)

    def go_left(self):
        self.setheading(W)
        self.forward(MOVE_DISTANCE)

    def go_right(self):
        self.setheading(E)
        self.forward(MOVE_DISTANCE)

