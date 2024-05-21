from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]



    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        self.segments.append(new_segment)

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].setpos(self.segments[i - 1].pos())
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].ycor() != self.segments[1].ycor() - 20:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].ycor() != self.segments[1].ycor() + 20:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].xcor() != self.segments[1].xcor() + 20:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].xcor() != self.segments[1].xcor() - 20:
            self.segments[0].setheading(0)



    def extend(self):
        self.add_segment(self.segments[-1].position())
        #add a new segment to the snake



