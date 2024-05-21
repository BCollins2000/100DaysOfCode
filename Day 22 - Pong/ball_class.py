from turtle import Turtle

NE = 45
NW = 135
SE = 315
SW = 225

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.setheading(45)


    def move(self):
        self.forward(5)

    def top_bot_bounce(self):
        if self.heading() == NW:
            self.setheading(SW)
        elif self.heading() == NE:
            self.setheading(SE)
        elif self.heading() == SW:
            self.setheading(NW)
        elif self.heading() == SE:
            self.setheading(NE)

    def side_bounce(self):
        if self.heading() == NW:
            self.setheading(NE)
            self.setx(-330)
        elif self.heading() == NE:
            self.setheading(NW)
            self.setx(330)
        elif self.heading() == SW:
            self.setheading(SE)
            self.setx(-330)
        elif self.heading() == SE:
            self.setheading(SW)
            self.setx(330)


    def reset_position(self):
        self.setpos(0,0)
        self.right(180)







