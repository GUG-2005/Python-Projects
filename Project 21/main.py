import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

sc = Screen()
sc.title("Turtle Racing Game")
sc.setup(width=600, height=600)
sc.tracer(0)

player = Player()
car_manager = CarManager()
sb = Scoreboard()

sc.listen()
sc.onkeypress(key="Up", fun=player.up)

game = True
num=0
while game:
    time.sleep(0.1)
    sc.update()
    num += 1
    if num % 5 == 0:
        car_manager.create()
    car_manager.move_cars()

    if player.ycor() > 280:
        player.leup()
        car_manager.leup()
        sb.update()

    for i in car_manager.all_cars:
        if player.distance(i) < 18:
            game = False
            sb.game_over()

sc.exitonclick()

