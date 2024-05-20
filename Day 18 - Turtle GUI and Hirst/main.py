from turtle import Turtle as t
from turtle import Screen as s
import random


tim = t()
tim.shape('turtle')
tim.color('dark violet')
tim.speed('fastest')
tim.width(5)



color_list = ['violet', 'indigo', 'blue',
       'green', 'yellow', 'orange', 'red']
angle_list = [180, 90, -90, 0]

# for step in range(100):
#     tim.color(random.choice(color_list))
#     tim.forward(30)
#     tim.right(random.choice(angle_list))



# for num_sides in range(3,15):
#     tim.color(random.choice(color_list))
#
#     for side in range(1,num_sides+1):
#         tim.forward(10)
#         tim.right(360/num_sides)
#     # tim.penup()
#     # tim.forward(10)
#     # tim.pendown()

num_circle = 35
for i in range(num_circle):
    tim.color(color_list[i % len(color_list)])
    tim.circle(250, extent=None, steps=None)
    tim.right(360/num_circle)








screen = s()
screen.exitonclick()