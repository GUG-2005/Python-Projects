from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def fow():
    t.forward(50)

def r():
    t.right(10)

def l():
    t.left(10)

def back():
    t.back(50)

screen.listen()
screen.onkey(key='w', fun=fow)
screen.onkeypress(key='a', fun=l)
screen.onkeypress(key='d', fun=r)
screen.onkey(key='s', fun=back)
screen.onkey(key='c', fun=screen.reset)
screen.exitonclick()