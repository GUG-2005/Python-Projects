from turtle import Turtle, Screen
import random

xa = -230
ya = -100
def turtle(color):
    t = Turtle()
    t.shape("turtle")
    t.color(color)
    t.penup()
    t.goto(x=xa, y=ya)
    all_turtles.append(t)

all_turtles = []
sc = Screen()
color = ["red", "orange", "yellow", "blue", "green", "violet"]
sc.setup(width=500,height=500)
sc.title("Turtle Racing game")
inp = sc.textinput(title="Pick one", prompt="Pick a color? And guess which turtle would win this race?")
for i in color:
    turtle(i)
    ya += 35

game = True
col = ""
while game:
    for i in all_turtles:
        dis = random.randint(0,10)
        i.forward(dis)
        if i.xcor() >= 230:
            game = False
            col = i.pencolor()

if col == inp:
    print(f"You've gone with winning colors")
else:
    print(f"There's nothing we can do for you!")