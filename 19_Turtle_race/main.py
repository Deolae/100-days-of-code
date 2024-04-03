from turtle import Turtle, Screen
import random

# Make the turtles list
turtles_list = []

# Make the turtle colors list
colors_list = ["red", "blue", "green", "purple", "yellow", "orange"]

# Screen setup
screen = Screen()
screen.title("Turtle Race")
screen.setup(width=500,height=400)

# Text prompt to get the bet from the user
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color from the following:"
                                                 "\n1- Red"
                                                 "\n2- Blue"
                                                 "\n3- Green"
                                                 "\n4- Purple"
                                                 "\n5- Yellow"
                                                 "\n6- Orange").lower()
# Function to make the turtles
def make_turtles():
    # Will be used to line up the turtles
    y_coord = -85

    # Make as many turtle objects as colors is in the colors list
    for i in range(0,len(colors_list)):
        # Append each turtle to the list with shape "turtle"
        turtles_list.append(Turtle(shape="turtle"))

        # Color the turtles
        turtles_list[i].color(colors_list[i])

        # Pen up while turtle goes to starting spot
        turtles_list[i].penup()

        # Move turtle to starting position
        turtles_list[i].goto(x=-230,y=y_coord)

        # add 40 to "y_coord" so the next turtle moves 40 paces up
        y_coord += 35

def start_race():
    race_on = True
    while race_on == True:
        # Check if any turtles reached the other side of the screen
        for turtle in turtles_list:
            if turtle.xcor() > 230:
                race_on = False
                winner = turtle.pencolor()
                if winner == user_bet:
                    print(f"You've won! the {winner} turtle is the winner!")
                else:
                    print(f"You've lost! the {winner} turtle is the winner!")

            # Move turtles a random distance between 1 and 8 paces
            turtle.forward(random.randint(1,8))

            # Give a random turtle a 4% chance for a 20 pace boost:
            random_chance = random.random()
            if random_chance <= 0.04:
                turtle.pendown()
                turtle.forward(20)
                turtle.penup()

# Make all the turtles and place them at starting spots
make_turtles()

# Start the race
start_race()

# Close screen on click
screen.exitonclick()