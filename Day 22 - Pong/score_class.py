from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color('orange')
        self.hideturtle()
        self.setpos(position)
        self.score_count = 0
        self.write(f"Score Count: {self.score_count}", font=("Verdana", 15, "normal"), align="center")

    def increase_score(self):
        self.clear()
        self.score_count += 1
        self.write(f"Score Count: {self.score_count}", font=("Verdana", 15, "normal"), align="center")

    def game_over(self):
        self.color('red')
        self.setpos(0, 0)
        self.write(f"GAME OVER", font=("Verdana", 30, "normal"), align="center")




