MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}
game = True
print("Welcome to Muthu Cafe")
while game == True:
    inp = input("With our three drinks(espresso/latte/cappuccino) type 1 or 2 or 3 to choose among? ")
    print("The digital money option in the machine got bankrupt and for the week please adjust with only coins! ")
    dimes = int(input("How many dimes would share with us? "))
    cents = int(input("How many cents would you like to share with us? "))
    quarters = int(input("How many quarters would you like to share with us? "))
    nickel = int(input("How many nickel would you like to share with us? "))
    resources["money"] = 0
    if inp == "report":
        for k in resources:
            print(f"{k}: {resources[k]}")
    else:
        inp = int(inp)
        money = (dimes*0.10) + (cents*0.01) + (quarters*0.25) + (nickel*0.05)
        num = 0
        global amnt, itm
        for i in MENU:
            if num == inp-1:
                amnt = MENU[i]["cost"]
                itm = i
            num += 1
        if money >= amnt:
            print(f"The remaining change in rupees is: ${money-amnt}")
            print(f"Enjoy your {itm}")
            resources["water"] = resources["water"] - MENU[itm]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU[itm]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU[itm]["ingredients"]["coffee"]
            resources["money"] = resources["money"] + amnt

        else:
            print("You don't have enough change for your drink! Sorry Mate please don't be hurted")
    g = input("Type 'yes' to operate for another drink and type 'no' to exit").lower()
    if g == "no":
        game = False