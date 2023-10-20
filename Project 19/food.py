from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.penup()
        self.mr()

    def mr(self):
        rand_x = randint(-230, 230)
        rand_y = randint(-230, 230)
        self.goto(rand_x, rand_y)