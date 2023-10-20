START = [(0, 0), (-20, 0), (-40, 0)]
MOVESPEED = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270


from turtle import Turtle
class Snake:

    def __init__(self):
        self.all_turtles = []
        self.create()
        self.head = self.all_turtles[0]

    def create(self):
        for i in START:
            self.add(i)

    def add(self, pos):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.goto(pos)
        self.all_turtles.append(t)

    def extend(self):
        ps= self.all_turtles[-1].pos()
        self.add(ps)

    def move(self):
        for i in range(len(self.all_turtles) - 1, 0, -1):
            pos = self.all_turtles[i - 1].pos()
            self.all_turtles[i].goto(pos)
        self.all_turtles[0].forward(MOVESPEED)

    def reset(self):
        for i in self.all_turtles:
            i.goto(1000,1000)
        self.all_turtles.clear()
        self.create()
        self.head = self.all_turtles[0]

    def right(self):
        if self.all_turtles[0].heading() != LEFT:
            self.all_turtles[0].setheading(RIGHT)

    def left(self):
        if self.all_turtles[0].heading() != RIGHT:
            self.all_turtles[0].setheading(LEFT)

    def up(self):
        if self.all_turtles[0].heading() != DOWN:
            self.all_turtles[0].setheading(UP)

    def down(self):
        if self.all_turtles[0].heading() != UP:
            self.all_turtles[0].setheading(DOWN)