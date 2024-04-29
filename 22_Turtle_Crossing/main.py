import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Osama's Turtle Crossing")
screen.tracer(0)

# Create player
player = Player()

# Create Scoreboard
scoreboard = Scoreboard()

# Create car manager
cars_manager = CarManager()

# Listen to key press from player, when player presses "w" move forward
screen.listen()
screen.onkeypress(fun=player.move_forward, key="w")
screen.onkeypress(fun=player.move_backward, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Move cars to other side of the screen
    cars_manager.create_car()
    cars_manager.move_cars()

    # If a player reached the end
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.update_level()
        car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT

    # If a player hit a car
    for car in cars_manager.all_cars:
        if player.distance(car) <= 20:
            game_is_on = False
            scoreboard.gameover()

screen.exitonclick()
