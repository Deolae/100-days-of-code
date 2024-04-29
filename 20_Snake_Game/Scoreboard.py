from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Times New Roman', 18, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,300)
        self.score = 0

    def displayScore(self):
        self.clear()
        self.pendown()
        self.write(arg=f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        self.penup()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER",align=ALIGNMENT,font=FONT)
