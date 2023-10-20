import turtle
import pandas

screen = turtle.Screen()
screen.title("US - States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
x = data["x"].to_list()
y = data["y"].to_list()
game = True
score = 0
correct = []
lives = 3
screen.tracer(0)
def create(i):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x[i], y[i])
    t.write(arg=f"{states[i]}", align="center", font=("Times New Roman", 10, 'normal'))

while game:
    answer = screen.textinput(title=f"{score}/50 States correct.({lives} lives)", prompt="Give a guess about a state? ").lower()
    if answer == "exit":
        game = False
        t = turtle.Turtle()
        t.penup()
        x = 295
        y = 265
        t.goto(x, y)
        t.pendown()
        t.pencolor("red")
        for i in range(50):
            newx = t.xcor() + 1
            newy = t.ycor() + 1
            t.goto(newx, newy)
        t.left(45)
        tu = turtle.Turtle()
        tu.penup()
        tu.goto(230, 265)
        tu.write(arg="Exit Here", align="left", font=("Algerian", 20, 'bold'))
        tu.hideturtle()
        screen.update()

        missing_states = [i for i in states if i not in correct]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missing states")
        correct.clear()
        missing_states.clear()


    for i in range(len(states)):
        if states[i].lower() == answer:
            correct.append(states[i])
            create(i)
            score += 1
            screen.update()

turtle.mainloop()
