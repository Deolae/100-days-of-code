import turtle
from turtle import Turtle, Screen
import random
import time

osama = Turtle()
osama.shape("turtle")
turtle.colormode(255)

# Draw a square
def square():
    for i in range(4):
        osama.forward(100)
        osama.right(90)

# Draw a dashed line
def dashed_line():
    for i in range(15):
        osama.pendown()
        osama.forward(10)
        osama.penup()
        osama.forward(10)

# Draw shapes
def shapes():
    # Define corners as 2 because it'll increase in first iteration
    corners = 2
    # Increase or decrease the number to add or remove shapes
    while corners < 9:
        # randomize a color
        osama.color(random.choice(colors))
        corners += 1
        # for the number of corners, draw lines to make the shape
        for i in range(0,corners):
            osama.forward(100)
            osama.right(360/corners)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomcolors = (r, g, b)
    return randomcolors

def random_walk():
    osama.pensize(5)
    osama.speed(100)
    directions = ["right","left"]
    # Change the number inside the range to decide how many lines the turtle makes
    for i in range(150):
        # randomize a direction
        random_direction = random.choice(directions)
        # randomize a color
        osama.color(random_color())
        # go forward by a random distance between 10 and 50 paces
        osama.forward(10 * random.randint(1,5))
        # Check which direction to turn and apply it
        if random_direction == "right":
            osama.right(90)
        elif random_direction == "left":
            osama.left(90)

# Draw a spirograph
def spirograph():
    osama.speed(50)
    osama.shape("classic")
    for i in range(0,360,5):
        osama.color(random_color())
        osama.circle(100)
        osama.setheading(i)
# Write a function name to draw what you like:
spirograph()
time.sleep(4)
osama.clear()
random_walk()

# Show the screen, and make it so that it closes on click
screen = Screen()
screen.exitonclick()
