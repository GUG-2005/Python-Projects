import random
from art import logo

print(logo)
rand_num = random.randint(0,101)
lives = 0
eoh = input("Before going into the game! Let's see would you like to play easy or hard? ").lower()
if eoh == 'easy':
    lives += 10
elif eoh == 'hard':
    lives += 5

game = True

while game == True and lives > 0:
    guess = int(input("Guess a Number! If it matches the correct answer? "))

    if guess > rand_num:
        print("Too High")
        lives -= 1
    elif guess < rand_num:
        print("Too Low")
        lives -= 1
    elif guess == rand_num:
        game = False
        print(f"You've guessed it right! The correct number is {rand_num}")

if lives == 0:
    print(f"You've lost the game! And the correct number {rand_num}")
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
