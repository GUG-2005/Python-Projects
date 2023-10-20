#Works only in relpit
from art import logo
from replit import clear

print(logo)
dict = {}
game = True

while game == True:
    name = input("What is the name of the bidder? ")
    bid = int(input("What is the bid from your side? $"))
    dict[name] = bid
    u = input("If there are any other bidders? Then give them your lap and wait for their ")
    if u == 'yes':
        clear()
    elif u == 'no':
        game = False
        max = 0
        for i in dict:
            if dict[i]>max:
                max = dict[i]
        user = ""
        for i in dict:
            if dict[i] == max:
                user = i
        print(f"The Auction is off! The highest bidder is {user}, with a price of {max}")


