from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()
        self.dotted_line()

    def update_score(self):
        self.clear()
        self.goto(x=80, y=200)
        self.write(self.left_score, align="center", font=("Courier", 70, "normal"))
        self.goto(x=-80, y=200)
        self.write(self.right_score, align="center", font=("Courier", 70, "normal"))

    def right_point(self):
        self.right_score+=1
        self.update_score()

    def left_point(self):
        self.left_score +=1
        self.update_score()

    def dotted_line(self):
        for i in range(-400,400,100):
            block = Turtle(shape="square")
            block.hideturtle()
            block.turtlesize(stretch_wid=3.5, stretch_len=0.1)
            block.color("white")
            block.penup()
            block.setpos(0, i)
            block.showturtle()