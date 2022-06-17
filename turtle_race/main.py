import turtle
from turtle import Turtle, Screen
import random

# my_turtle = input("Bet on a turtle (Purple, Blue, Sky Blue, Green, Yellow, Orange, Red): ").lower()
#
# to_continue = True
#
# while to_continue:
#     screen = Screen()
#
#     purple = Turtle()
#     purple.color("purple")
#     purple.shape("turtle")
#     purple.penup()
#     purple.setx(-(screen.window_height()) / 2)
#     purple.sety(150)
#
#     blue = Turtle()
#     blue.color("blue")
#     blue.shape("turtle")
#     blue.penup()
#     blue.setx(-(screen.window_height()) / 2)
#     blue.sety(100)
#
#     sky_blue = Turtle()
#     sky_blue.color("sky blue")
#     sky_blue.shape("turtle")
#     sky_blue.penup()
#     sky_blue.setx(-(screen.window_height()) / 2)
#     sky_blue.sety(50)
#
#     green = Turtle()
#     green.color("green")
#     green.shape("turtle")
#     green.penup()
#     green.setx(-(screen.window_height()) / 2)
#
#     yellow = Turtle()
#     yellow.color("yellow")
#     yellow.shape("turtle")
#     yellow.penup()
#     yellow.setx(-(screen.window_height()) / 2)
#     yellow.sety(-50)
#
#     orange = Turtle()
#     orange.color("orange")
#     orange.shape("turtle")
#     orange.penup()
#     orange.setx(-(screen.window_height()) / 2)
#     orange.sety(-100)
#
#     red = Turtle()
#     red.color("red")
#     red.shape("turtle")
#     red.penup()
#     red.setx(-(screen.window_height()) / 2)
#     red.sety(-150)
#
#     screen.listen()
#
#     step = [1, 1, 5, 5, 10, 15, 20, 25, 30]
#
#     final_pos = (screen.window_width()) / 2
#
#
#     def game_over():
#         game_over_indicator = 0
#         if purple.xcor() > final_pos:
#             game_over_indicator += 1
#             if my_turtle == "purple":
#                 print("You Won!")
#             else:
#                 print("Sorry! You lost!!\nThe winner in Purple!!!")
#             return True
#         if blue.xcor() > final_pos:
#             game_over_indicator += 1
#             if my_turtle == "blue":
#                 print("You Won!")
#             else:
#                 print("Sorry! You lost!!\nThe winner in Blue!!!")
#             return True
#         if sky_blue.xcor() > final_pos:
#             game_over_indicator += 1
#             if my_turtle == "sky blue":
#                 print("You Won!")
#             else:
#                 print("Sorry! You lost!!\nThe winner in Sky Blue!!!")
#             return True
#         if green.xcor() > final_pos:
#             game_over_indicator += 1
#             if my_turtle == "green":
#                 print("You Won!")
#             else:
#                 print("Sorry! You lost!!\nThe winner in Green!!!")
#             return True
#         if yellow.xcor() > final_pos:
#             game_over_indicator += 1
#             if my_turtle == "yellow":
#                 print("You Won!")
#             else:
#                 print("Sorry! You lost!!\nThe winner in Yellow!!!")
#             return True
#         if orange.xcor() > final_pos:
#             game_over_indicator += 1
#             if my_turtle == "orange":
#                 print("You Won!")
#             else:
#                 print("Sorry! You lost!!\nThe winner in Orange!!!")
#             return True
#         if red.xcor() > final_pos:
#             game_over_indicator += 1
#             if my_turtle == "red":
#                 print("You Won!")
#             else:
#                 print("Sorry! You lost!!\nThe winner in Red!!!")
#             return True
#         if game_over_indicator == 0:
#             return False
#
#
#     while game_over() is False:
#         purple.forward(random.choice(step))
#         blue.forward(random.choice(step))
#         sky_blue.forward(random.choice(step))
#         green.forward(random.choice(step))
#         yellow.forward(random.choice(step))
#         orange.forward(random.choice(step))
#         red.forward(random.choice(step))
#
#     screen.exitonclick()
#
#     break
#
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race. Pick a color: ")
colors = ["red", "orange", "blue", "yellow", "green", "purple"]

all_turtles = []
y_cor = - 130
for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-240, y=y_cor)
    y_cor += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"The winning turtle is {turtle.pencolor()}. You've won!!")
            else:
                print(f"The winning turtle is {turtle.pencolor()}. You've lost!!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
