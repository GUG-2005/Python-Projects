import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]
inp = int(input("Type 1 for Rock,2 for paper, 3 for scissors chose what you feel! "))
print(rps[inp-1])

rand_num = random.randint(1, 3)
print(rps[rand_num-1])

if inp>rand_num:
    print("You won")
elif inp == rand_num:
    print("Its a draw")
else:
    print("You Lose")
