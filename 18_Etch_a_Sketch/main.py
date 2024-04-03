from turtle import Turtle, Screen

# Create turtle and screen objects
osama_turtle = Turtle()
screen = Screen()

# Move forward function
def move_forward():
    osama_turtle.forward(30)

# Move backward function
def move_backward():
    osama_turtle.backward(30)

# Turn left function
def turn_left():
    osama_turtle.left(10)

# Turn right function
def turn_right():
    osama_turtle.right(10)

# Clear the screen and reset turtle position
def clear_screen():
    osama_turtle.clear()
    osama_turtle.penup()
    osama_turtle.home()
    osama_turtle.pendown()

# Listen to user
screen.listen()

# On user click functions
screen.onkeypress(key="w",fun=move_forward)
screen.onkeypress(key="s",fun=move_backward)
screen.onkeypress(key="a",fun=turn_left)
screen.onkeypress(key="d",fun=turn_right)
screen.onkeypress(key="c",fun=clear_screen)

# Exit screen on mouse click
screen.exitonclick()
