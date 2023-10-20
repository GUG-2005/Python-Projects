# Use it only in Repilt
from art import logo, vs
from data import data
import replit
from random import randint

game = True
score = 0
print(logo)
rand_num1 = randint(0, len(data)-1)
while game == True:
    rand_num2 = randint(0, len(data) - 1)
    print(f"Score : {score}")
    print(f'Compare A: {data[rand_num1]["name"]}, {data[rand_num1]["description"]} and they are from {data[rand_num1]["country"]}')
    n1 = data[rand_num1]["follower_count"]
    n2 = data[rand_num2]["follower_count"]

    print(vs)
    if rand_num1 == rand_num2:
        rand_num2 = randint(0, len(data)-1)

    print(f'Compare B: {data[rand_num2]["name"]}, {data[rand_num2]["description"]} and they are from {data[rand_num2]["country"]}')

    inp = input("Type A (or) B to choose who has more followers!? ").lower()
    if inp == "a" and n1>n2:
        print("You guessed it right! And your score is incremented!")
        score += 1
        replit.clear()
    elif inp == "b" and n2>n1:
        print("You guessed it right! And your score is incremented!")
        score += 1
        rand_num1 = rand_num2
        replit.clear()
    else:
        print(f"You lost the game! And your score is {score}")
        game = False