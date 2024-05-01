from turtle import Screen, Turtle
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

# Create screen and setup
screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor("black")
screen.title("Osama's Snake Game")
screen.tracer(0)

# Create the snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

# Makes the screen listen to key strokes and move the snake accordingly
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

# While game is not over, keep running
gameover = False
while gameover == False:
    # Update screen, display score, then sleep for 0.2 seconds
    scoreboard.displayScore()
    screen.update()
    time.sleep(0.1)

    # Keep moving the snake
    snake.move()

    # Detect collison with food
    if snake.snake_parts[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score += 1

    # Detect collison with wall
    snake_head = snake.snake_parts[0]
    if snake_head.xcor() >= 330 or snake_head.xcor() <= -330 or snake_head.ycor() >= 330 or snake_head.ycor() <= -330:
        scoreboard.reset()
        snake.reset()

    # Detect collison with tail
    for segment in snake.snake_parts[1:]:
        if snake_head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()