from turtle import Turtle

PADDLE_SPEED = 20
class Paddle(Turtle):
    def __init__(self,x_pos,y_pos):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.paddle_position(x_pos,y_pos)
        self.showturtle()

    def paddle_position(self,x_pos,y_pos):
        self.setpos(x=x_pos,y=y_pos)

    def go_up(self):
        if self.ycor() < 260:
            y_new = self.ycor() + PADDLE_SPEED
            self.goto(x=self.xcor(),y=y_new)

    def go_down(self):
        if self.ycor() > -260:
            y_new = self.ycor() - PADDLE_SPEED
            self.goto(x=self.xcor(),y=y_new)
