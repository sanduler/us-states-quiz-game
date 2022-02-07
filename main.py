# Name: Ruben Sanduleac
# Date: February 6th, 2021
# Description: This program is a game that lets the user guess the States in the United States.
#              The player is able to see the GUI through the turtle library and the data is processed
#              and analyzed through the pandas library.
import turtle

import pandas
from turtle import Turtle, Screen

screen = Screen()
pen = Turtle()
pen.hideturtle()
score = 0
# rename the title of the Quiz
screen.title("U.S. States Quiz")
# get the directory into a variable
quiz_image = "./img/blank_states_img.gif"
# add the shape to the screen
screen.addshape(quiz_image)
# print the turtle on the screen
turtle.shape(quiz_image)
US_data = pandas.read_csv("./data/50_states.csv")
# print(US_data.state[1])
all_the_states = US_data.state.to_list()
# list of all correct guesses
guess_list = []
while len(guess_list) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt=f"What is another State's name? {len(guess_list)}/50").title()
    # if user types exit the game breaks
    if answer_state == "Exit":
        break
    if answer_state in all_the_states:
        # not to draw on the screen
        pen.penup()
        # get all the info the state that matches the if statement
        state_data = US_data[US_data.state == answer_state]
        # go to the x and y on the state from the csv file in data
        pen.goto(int(state_data.x), int(state_data.y))
        # write the answer on the screen
        pen.write(answer_state)
        # append the correct answer to a list
        guess_list.append(answer_state)


# state_to_learn after the user clicks exit
to_learn = []

# loop through all the states and check if they have any states that they didnt answer
for states in US_data.state:
    if states not in guess_list:
        to_learn.append(states)

# create a new data for csv
new_data = pandas.DataFrame(to_learn)
new_data.to_csv("states_to_learn.csv")
