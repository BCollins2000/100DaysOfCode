from turtle import Screen, Turtle
import time
from snake_class import Snake
from food_class import Food
from score_class import Score


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Epic Snake Game!!")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

food = Food()
score = Score()
play_game = True
while play_game:
    screen.update()
    time.sleep(.1)
    snake.move()
    # Detect snake collision with food:
    if snake.head.distance(food) < 1:
        print("nom nom nom.")
        food.refresh()
        score.increase_score()
        snake.extend()
    if abs(snake.head.xcor()) > 300 or abs(snake.head.ycor()) > 300:
        play_game = False
        score.game_over()
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 1:
            play_game = False
            score.game_over()









screen.exitonclick()