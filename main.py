import turtle
from turtle import Turtle, Screen

import pandas

screen = Screen()

screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states = 0
states_list = []

marker = Turtle()
marker.ht()

data = pandas.read_csv("50_states.csv")

def marking_states(guessed_state):
    x_cor = data[data.state == f"{guessed_state}"].x.item()
    y_cor = data[data.state == f"{guessed_state}"].y.item()
    marker.color("Black")
    marker.penup()
    marker.goto(x_cor, y_cor)
    marker.write(arg=f"{guessed_state}", align="Center")
    

correct = True
while correct:
    guessed_state = screen.textinput(title="Guess the state", prompt="What's another state name?").title()
    while guessed_state in states_list:
        guessed_state = screen.textinput(title="Already Guessed", prompt="You already guessed that state! Try again.").title()
        marking_states(guessed_state)
    if guessed_state in data["state"].values and guessed_state not in states_list:
        states_list.append(guessed_state)
        marking_states(guessed_state)
        states += 1
        screen.title(f"{states}/50 States Correct")
        if states == 50:
            screen.textinput(title="Congratulations!", prompt="You guessed all the states! Press OK to exit.")
            break
        screen.update()
    else:
        guessed_state = screen.textinput(title="Wrong State", prompt="Try again!").title()
        marking_states(guessed_state)

















screen.exitonclick()