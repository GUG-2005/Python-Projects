COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random
class CarManager:

    def __init__(self):
        self.all_cars = []
        self.start = STARTING_MOVE_DISTANCE

    def create(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        self.y = random.randint(-240, 280)
        new_car.goto(300, self.y)
        new_car.color(random.choice(COLORS))
        self.all_cars.append(new_car)

    def move_cars(self):
        for i in self.all_cars:
            i.setheading(180)
            i.forward(self.start)

    def leup(self):
        self.start = self.start + MOVE_INCREMENT
