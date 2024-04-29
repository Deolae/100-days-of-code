from turtle import Turtle

BALL_SPEED = 4 # Changes ball speed
SLEEP_TIME = 0.02 # match in line 42 as well
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED
        self.move_speed = SLEEP_TIME

    def move(self,direction):

        # Move the ball to the top right corner
        if direction == "right":
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x,new_y)

        # Move the ball to the top left corner
        if direction == "left":
            new_x = self.xcor() - self.x_move
            new_y = self.ycor() - self.y_move

            self.goto(new_x, new_y)

    def bounce_y(self):
        # Reverse the direction
        self.y_move *= -1

    def bounce_x(self):
        # Speed up
        self.move_speed *= 0.85
        # Reverse the direction
        self.x_move *= -1

    def reset_position(self):
        self.setpos(0,0)
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED
        self.move_speed = SLEEP_TIME
        self.bounce_x()