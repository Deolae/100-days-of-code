from turtle import Turtle
from random import Random
from scoreboard import Scoreboard
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
random = Random()
scoreboard = Scoreboard()
scoreboard.clear()


class CarManager():
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_number = random.randint(1, 8) # 37% chance for car to spawn
        if random_number <= 3:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_coord = random.randint(a=-250, b=250)
            new_car.goto(x=300, y=y_coord)
            new_car.showturtle()
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
