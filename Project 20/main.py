from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

sc = Screen()
sc.title("Pong Game")
sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.tracer(0)

l_p = Paddle((-350, 0))
r_p = Paddle((350, 0))
ball = Ball()
score = Score()

sc.listen()
sc.onkey(fun=l_p.up, key="w")
sc.onkey(fun=l_p.down, key="s")
sc.onkey(fun=r_p.up, key="Up")
sc.onkey(fun=r_p.down, key="Down")



game = True
while game:
    sc.update()
    time.sleep(ball.move)
    ball.mov()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 380:
        score.update_l()
        ball.goto(0, 0)
        ball.bounce_x()
        ball.bounce_y()

    if ball.xcor() < -380:
        score.update_r()
        ball.goto(0, 0)
        ball.bounce_x()
        ball.bounce_y()

    if ball.distance(r_p) < 25 and ball.xcor() > 335 or ball.distance(l_p) < 25 and ball.xcor() < -335:
        ball.bounce_x()



sc.exitonclick()