from art import logo

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

o = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
def calc():
    game = True
    print(logo)
    n1 = float(input("Give us the 1st number to serve you! "))

    for i in o:
        print(i)
    while game == True:
        o_inp = input("Now you need to feed us a symbol! To perform the proper operation? ")
        n2 = float(input("Now it's time for the 2nd number! "))
        ret_fun = o[o_inp]
        ans = ret_fun(n1, n2)

        print(f"{n1} {o_inp} {n2} = {ans}")

        inp = input(f"Would you like to continue the calculation with {ans} or you'd like to move on with a new one? ").lower()

        if inp == "yes":
            n1 = ans
        else:
            game = False
            # clear() function can be used in replit
            calc()

calc()
