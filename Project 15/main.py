from turtle import Turtle, Screen
import prettytable


table = prettytable.PrettyTable()
table.add_column("Pokemon name",["Pikachu","Charmander", "Charizard"])
table.add_column("Type",["Electric","Fire", "Fire"])
table.align = "l"
print(table)

# t = Turtle()
# sc = Screen()
#
# t.shape("turtle")
# t.color("green")
# t.forward(100)
#
# sc.exitonclick()
