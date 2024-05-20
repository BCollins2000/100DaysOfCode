# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('dots_fun.jpg', 25)
#
# # color_list = []
# # for color in colors:
# #     red = color.rgb.r
# #     green = color.rgb.g
# #     blue = color.rgb.b
# #     color_tuple = (red, green, blue)
# #     color_list.append(color_tuple)
# # print(color_list)

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]

#
# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34
#
# # RGB and HSL are named tuples, so values can be accessed as properties.
# # These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s

import turtle
from turtle import Turtle as t
from turtle import Screen as s
import random
turtle.colormode(255)
tim = t()
#tim.colormode(255)
tim.shape('turtle')
tim.color('dark violet')
tim.speed('fastest')
tim.width(5)
tim.hideturtle()

tim.penup()

start_x = -250
start_y = -250
for y in range(0,10):
    for x in range(0,10):
        tim.goto(start_x + 50 * x, start_y + 50 * y)
        tim.pendown()
        color = random.choice(color_list)
        tim.color(color)
        tim.fillcolor(color)
        tim.begin_fill()
        tim.circle(10, extent=None, steps=None)
        tim.end_fill()
        tim.penup()





screen = s()
screen.exitonclick()