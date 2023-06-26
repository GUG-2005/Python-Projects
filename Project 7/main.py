#Step 1
import random
from art import logo, stages
from words import word_list
print(logo)

lives = 6
chosen_word = random.choice(word_list)
game = False
display = []
for i in range(0, len(chosen_word)):
    display += "_"

while game == False:
    guess = input("Welcome to the Game! Let's start by guessing a letter? ").lower()
    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            print(f'The guessed letter {guess} is in the letter')
            display[i] = chosen_word[i]

    if guess not in chosen_word:
        print(stages[lives])
        lives -= 1
        print("The letter is not in the word! Don't lose Hope ! Try Again")

    if lives == 0:
        print(stages[0])
        print("You Lose! Game Over, mate!")
        print(f"The word is {chosen_word}")
        game = True

    if "_" not in display:
        game = True
        print("You Win")

    print(' '.join(display))

