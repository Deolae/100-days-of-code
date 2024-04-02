import turtle
from playsound import playsound
import colorgram
import random
from turtle import Turtle, Screen

# Extracting colors from a Hirst Painting
def extract_colors(image, number_of_Colors):
    global colors
    '''Returns RGB colors from a picture in a tuple'''
    image_colors = colorgram.extract(image, 30)
    colors = []
    for color in image_colors:
        color = (color.rgb.r, color.rgb.g, color.rgb.b)
        if color[0] > 240 or color[1] > 240 or color[2] > 240:
            pass
        else:
            colors.append(color)
    # Remove first item because it's the white colors
    colors.pop(0)
    print(colors)

# Make the turtle vibrate then poof!
def turtle_poof():
    # for silly sound at the end uncomment this:
    playsound("MICHAELDON'TLEAVEMEHERE.wav", False)
    pos = osama_turtle.pos()
    for i in range(0, 360, 2):
        random_direction = random.randint(0, 15)
        osama_turtle.setpos(pos[0] + random_direction, pos[1] + random_direction)
        osama_turtle.tiltangle(i)
    osama_turtle.hideturtle()


# Drawing the painting
def hirst_painting():
    global osama_turtle
    # Set color mode to RGB
    turtle.colormode(255)
    # Make a turtle object
    osama_turtle = Turtle()
    osama_turtle.speed(300)
    osama_turtle.shape("turtle")
    # Lift pen up to not draw while changing position
    osama_turtle.penup()
    # coords of the bottom left of canvas
    position_x = -250
    position_y = -250
    # once 10 rows have been made, stop the loop
    rows = 0
    while rows < 10:
        # Set turtle positiong
        osama_turtle.setpos(position_x,position_y)
        for i in range (0,10):
            osama_turtle.pencolor(random.choice(colors))
            osama_turtle.dot(size=20)
            osama_turtle.forward(50)
        # take turtle up the original position by 50 paces
        position_y += 50
        rows += 1
    # Turtle goes poof at the end!
    turtle_poof()

# Start Program
extract_colors("hirst.png",20)
hirst_painting()

# Show the screen, and make it close on click
screen = Screen()
screen.exitonclick()
