# Name: Ruben Sanduleac
# Date: February 6th, 2021
# Description: This program is a game that lets the user guess the States in the United States.
#              The player is able to see the GUI through the turtle library and the data is processed
#              and anylized through the pandas library.
import turtle

import pandas
from turtle import Turtle, Screen

screen = Screen()
pen = Turtle()
pen.hideturtle()
score = 0
# rename the title of the Quiz
screen.title(f"{score}/50 U.S. States Quiz")
# get the directory into a variable
quiz_image = "./img/blank_states_img.gif"
# add the shape to the screen
screen.addshape(quiz_image)
# print the turtle on the screen
turtle.shape(quiz_image)
US_data = pandas.read_csv("./data/50_states.csv")
# print(US_data.state[1])
game_is_playing = True
guess_list = []
while game_is_playing:
    answer_state = screen.textinput(title="Guess the State", prompt="What is another State's name?").title()
    # print(US_data.x[1])
    for state in US_data.state:
        if state == answer_state:

            location = (US_data[US_data.state == str(state)])
            # print(location.x)
            location_x = int(location.x)
            location_y = int(location.y)
            # print(location_x)
            guess_list.append(state)
            pen.penup()
            pen.goto(location_x, location_y)
            pen.pendown()
            pen.write(state, font=("Calibri", 8, "bold"))
            score += 1





turtle.mainloop()
