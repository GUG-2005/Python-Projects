from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.goto(0, 0)
        self.color("white")
        self.x = 1
        self.y = 1
        self.move = 0.00001

    def mov(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.move *= 0.85

