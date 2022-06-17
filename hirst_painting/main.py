# import colorgram
#
# color = colorgram.extract("hirst's painting.jpg", 40)
#
#
# colors = []
#
# for rgbs in color:
#     r = rgbs.rgb.r
#     g = rgbs.rgb.g
#     b = rgbs.rgb.b
#     color_tuple = (r, g, b)
#     colors.append(color_tuple)
#
# print(colors)
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
screen = Screen()

tim = Turtle()

color_list = [(214, 154, 105), (49, 96, 139), (163, 80, 45), (223, 209, 107), (17, 36, 59), (185, 163, 25),
              (120, 163, 202), (56, 30, 18), (126, 68, 94), (210, 91, 69), (43, 128, 70), (193, 140, 160),
              (162, 20, 10), (125, 181, 156), (58, 28, 40), (129, 26, 42), (19, 52, 43), (194, 91, 113), (48, 170, 98),
              (39, 62, 97), (27, 91, 52), (235, 162, 187), (108, 118, 172), (225, 206, 2), (6, 88, 108),
              (227, 179, 170), (65, 81, 31), (140, 214, 195), (170, 183, 217), (54, 146, 192), (165, 203, 213)]


def set_position():
    tim.penup()
    tim.setx(-225)
    y = tim.ycor()
    tim.sety(y + 50)


tim.hideturtle()
tim.penup()
tim.setx(-225)
tim.sety(-225)

for _ in range(10):
    for _ in range(10):
        tim.showturtle()
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
        tim.hideturtle()

    set_position()

tim.hideturtle()
screen.exitonclick()
