from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create screen and setup
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Osama's Pong Game")

# Create the Paddle
player1 = Paddle(x_pos=-350, y_pos=0)
player2 = Paddle(x_pos=350,y_pos=0)

# Create the Ball
ball = Ball()

# Create the Scoreboard
scoreboard = Scoreboard()

# Makes the screen listen to key strokes and move the paddle accordingly
screen.listen()
screen.onkeypress(player1.go_up, "w")
screen.onkeypress(player1.go_down, "s")
screen.onkeypress(player2.go_up, "Up")
screen.onkeypress(player2.go_down, "Down")

gameover = False
while gameover == False:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move("right")

    # Detect collison with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collison with paddle
    if (ball.distance(player2) < 55 and ball.xcor() > 320 and ball.xcor() < 350) or (
            ball.distance(player1) < 55 and ball.xcor() < -320 and ball.xcor() > -350):
        ball.bounce_x()

    # Detect if ball scored in right side
    if ball.xcor() > 390:
        scoreboard.left_point()
        ball.reset_position()

    # Detect if ball scored in left side
    if  ball.xcor() < -390:
        scoreboard.right_point()
        ball.reset_position()

screen.exitonclick()