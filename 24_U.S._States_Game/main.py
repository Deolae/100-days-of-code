# Import libraries
import turtle
import pandas as pd
from answer_turtle import AnswerTurtle

# Create the dataframe for the states
states = pd.read_csv("50_states.csv")

# Create and setup screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# And the U.S. map image as a shape to be displayed
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Variables to count correctly answered states
correct_answer = 0
correct_states = []
while correct_answer <50:
    # Get input from user
    answer_state = screen.textinput(title=f"{correct_answer}/50 states guessed",
                                    prompt="What's another state's name?\n type 'exit' to quit the game'").capitalize()

    # Exit the game if user types "Exit"
    if answer_state == "Exit":
        break

    # loop to get state name, x value, and y value
    for index, state_row in states.iterrows():
        x_state = state_row["x"]
        y_state = state_row["y"]
        state_name = state_row["state"]

        # Compare user guess with state names
        if state_name == answer_state and answer_state not in correct_states:
            correct_answer+=1
            correct_states.append(answer_state)
            AnswerTurtle(x_cor=x_state, y_cor=y_state, stateName=state_name)

# Save the missing states the user didn't guess in a csv
missed_states =[]
for state in states["state"]:
    if state not in correct_states:
        missed_states.append(state)

df = pd.DataFrame(data=missed_states)
df.to_csv("States_to_Learn.csv")
