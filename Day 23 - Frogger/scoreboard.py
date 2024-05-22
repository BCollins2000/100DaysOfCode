from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position, title):
        super().__init__()
        self.penup()
        self.color('orange')
        self.hideturtle()
        self.title = title
        self.setpos(position)
        self.score_count = 0
        self.write(f"{self.title}: {self.score_count}", font=("Verdana", 15, "normal"), align="center")

    def increase_score(self):
        self.clear()
        self.score_count += 1
        self.write(f"{self.title}: {self.score_count}", font=("Verdana", 15, "normal"), align="center")

    def refresh_score(self):
        self.clear()
        self.write(f"{self.title}: {self.score_count}", font=("Verdana", 15, "normal"), align="center")

    def game_over(self):
        self.color('red')
        self.setpos(0, 0)
        self.write(f"GAME OVER", font=("Verdana", 30, "normal"), align="center")

class GoalLine(Turtle):
    def __init__(self, ycord):
        super().__init__()
        self.color('green')
        self.pensize(15)
        self.penup()
        self.setpos(-320, ycord)
        self.pendown()
        self.goto(320, ycord)

