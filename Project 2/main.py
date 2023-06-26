#If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to our Tip Calculator! \n\n")

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
total = int(input("Help yourself! Now tell what is the total bill? $"))
n = int(input("Ok Ok, That's good your bill is " + str(total) + "! How many people are splitting it? "))
tip = int(input("Ok that's good! Do you tip? And if you'd like to tip what will be that tip percentage? "))

split = float((total/n) * ((tip/100) + 1))
print("Ok now your total is $" + str(round(split, 2)))
print("Thankyou, for visiting us Sir! Hoping for you to return...!")
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇