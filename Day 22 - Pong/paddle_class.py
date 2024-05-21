from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.setpos(position)
        self.shape('square')
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.shapesize(1, 5)
        self.setheading(90)


    def go_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)






