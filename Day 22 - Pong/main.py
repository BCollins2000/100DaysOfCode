from turtle import Screen, Turtle
from paddle_class import Paddle
from ball_class import Ball
from score_class import Score
import time



screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("The Epic Pong Game!!")
screen.tracer(0)


pad_1 = Paddle((-350,0))
pad_2 = Paddle((350,0))
ball = Ball()

screen.listen()
screen.onkey(pad_1.go_up,"w")
screen.onkey(pad_1.go_down,"s")
screen.onkey(pad_2.go_up,"Up")
screen.onkey(pad_2.go_down,"Down")

score_left = Score((-200,275))
score_right = Score((200,275))

game_is_on = True
while game_is_on == True:
    screen.update()
    time.sleep(.01)
    ball.move()
    if abs(ball.ycor()) > 280 :
        ball.top_bot_bounce()
    if abs(ball.xcor() - pad_1.xcor()) < 20 and abs(ball.ycor() - pad_1.ycor()) < 30:
        ball.side_bounce()
    if abs(ball.xcor() - pad_2.xcor()) < 20 and abs(ball.ycor() - pad_2.ycor()) < 30:
        ball.side_bounce()
    if ball.xcor() > 380:
       ball.reset_position()
       score_left.increase_score()
    if ball.xcor() < -380:
       ball.reset_position()
       score_right.increase_score()





screen.exitonclick()