from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

sc = Screen()
sc.title("Snake Game")
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.tracer(0)

snake = Snake()
food = Food()
score = Score()

sc.listen()
sc.onkey(fun=snake.up, key="Up")
sc.onkey(fun=snake.down, key="Down")
sc.onkey(fun=snake.left, key="Left")
sc.onkey(fun=snake.right, key="Right")

game = True
while game:
    sc.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.mr()
        score.increase()
        snake.extend()

    if snake.head.xcor() >280 or snake.head.xcor() < -295 or snake.head.ycor() > 298 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for seg in snake.all_turtles[1:]:
        if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()

sc.exitonclick()