# Name: Ruben Sanduleac
# Date: February 6th, 2021
# Description: This program is a game that lets the user guess the States in the United States.
#              The player is able to see the GUI through the turtle library and the data is processed
#              and anylized through the pandas library.
import turtle

import pandas
from turtle import Turtle, Screen

screen = Screen()
# rename the title of the Quiz
screen.title("U.S. States Quiz")
# get the directory into a variable
quiz_image = "./img/blank_states_img.gif"
# add the shape to the screen
screen.addshape(quiz_image)
# print the turtle on the screen
turtle.shape(quiz_image)


answer_state = screen.textinput(title="Guess the State", prompt="What is another State's name?")
turtle.mainloop()
