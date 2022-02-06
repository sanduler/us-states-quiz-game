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
all_the_states = US_data.state.to_list()
guess_list = []
while len(guess_list) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What is another State's name?").title()
    if answer_state in all_the_states:
        pen.penup()
        state_data = US_data[US_data.state == answer_state]
        pen.goto(int(state_data.x), int(state_data.y))
        pen.write(answer_state)
        guess_list.append(answer_state)



turtle.mainloop()
