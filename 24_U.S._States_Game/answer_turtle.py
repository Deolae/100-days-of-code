from turtle import Turtle


class AnswerTurtle(Turtle):
    def __init__(self, x_cor, y_cor, stateName):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=x_cor, y=y_cor)
        self.write(arg=stateName, align="center")

