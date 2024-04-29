from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-230,y=260)
        self.level = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.level +=1
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=FONT)
