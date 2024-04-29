from turtle import Turtle

MOVE_POSITION= 21
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    # Make the starting snake body and set coordinates
    def __init__(self):
        global snake_parts
        self.snake_parts = []
        self.current_part = {"y": 0, "x": 0}
        for i in range(3):
            # Make the part and put it in list
            body_part = Turtle(shape="square")
            body_part.color("white")
            body_part.penup()
            self.snake_parts.append(body_part)
            # Add the part to the canvas and move the coordinates for the next one
            self.snake_parts[i].setx(self.current_part["x"])
            self.current_part["x"] -= MOVE_POSITION

    def extend(self):
        '''Add a new segment to the snake'''
        self.add_segment(self.snake_parts[-1].position())

    def add_segment(self, position):
        body_part = Turtle(shape="square")
        body_part.color("white")
        body_part.penup()
        body_part.goto(position)
        self.snake_parts.append(body_part)

    def move(self):
            # Move each part to the position of the part in front of it (to follow each other)
            for part in range(len(self.snake_parts) - 1, 0, -1):
                new_x = self.snake_parts[part - 1].xcor()
                new_y = self.snake_parts[part - 1].ycor()
                self.snake_parts[part].goto(new_x, new_y)
            self.snake_parts[0].forward(MOVE_POSITION)

    # Turn North
    def up(self):
        if self.snake_parts[0].heading() != DOWN:
            self.snake_parts[0].setheading(UP)

    # Turn South
    def down(self):
        if self.snake_parts[0].heading() != UP:
            self.snake_parts[0].setheading(DOWN)

     # Turn West
    def left(self):
        if self.snake_parts[0].heading() != RIGHT:
            self.snake_parts[0].setheading(LEFT)

    # Turn East
    def right(self):
        if self.snake_parts[0].heading() != LEFT:
            self.snake_parts[0].setheading(RIGHT)