from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, tup):
        super().__init__()
        self.xy = (tup)
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(self.xy)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed("fastest")

    def up(self):
        x = self.xcor()
        y = self.ycor() + 25
        self.goto(x, y)

    def down(self):
        x = self.xcor()
        y = self.ycor() - 25
        self.goto(x, y)