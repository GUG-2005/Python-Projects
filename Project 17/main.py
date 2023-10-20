from turtle import Turtle, Screen
import random

turtle = Turtle()
sc = Screen()
turtle.penup()
xa = -250
ya = -250
col = ["lime green", "gold", "orange red", "green yellow", "dark violet", "red", "blue","light blue","grey"]

turtle.goto(xa, ya)
turtle.dot(20, random.choice(col))
def go(xa, ya):
    turtle.goto(xa, ya)
    turtle.dot(20, random.choice(col))

for i in range(0, 11):
    for j in range(0, 9):
        xa = xa + 50
        if xa > 200:
            xa = -250
            ya = ya + 50
        go(xa, ya)
sc.exitonclick()


