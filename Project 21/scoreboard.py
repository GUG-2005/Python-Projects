FONT = ("Courier", 24, "normal")
START = (-205, 235)

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(START)
        self.score = 0
        self.write(arg=f"Score: {self.score}", align="center", font=FONT)


    def update(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over!!", align="center", font=FONT)