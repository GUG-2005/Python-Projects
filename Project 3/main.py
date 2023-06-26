print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("\nAppreciating that you chose an Adventure! Thank you Travelling with me!")
dir1 = input("But now you have to chose your own path, Would you like to go left or right ").lower()
if dir1 == "left":
    dir2 = input(("You've reached a river bank, Do you have the patience to wait for a boat or swim across? ")).lower()
    if dir2 == "wait":
        dir3= input("You've successfully reached the ancient tamil temple, Red, Blue and Yelllow coloured Doors Choose wisey? ").lower()
        if dir3 == "yellow":
            print("Congragulations! You've found the ancient treasure!")
        elif dir3 == "blue":
            print("Eaten by ancient beast! You Lose! Good Fight though! ")
        elif dir3 == "red":
            print("Burnt by fire! No Idea of how you managed to survive the game so far!")
        else:
            print("You Lose.")
    else:
        print("You are a good bait for the hungry Crocs! So its Game Over!")
else:
    print("You fell into a hole! Game Over!")
