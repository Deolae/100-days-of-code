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
        with open("data.txt",mode="r") as high:
            self.highscore = int(high.read())

    def displayScore(self):
        self.clear()
        self.goto(0, 300)
        with open("data.txt", mode="r") as high:
            self.highscore = int(high.read())
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}",align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.highscore:
            with open ("data.txt", mode="w") as high:
                high.write(str(self.score))
        self.score = 0
        self.goto(0,0)
        self.write(arg="GAME OVER",align=ALIGNMENT,font=FONT)
