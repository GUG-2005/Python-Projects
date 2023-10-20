import pandas

gray = 0
red = 0
black = 0
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_list = data["Primary Fur Color"].to_list()
for i in color_list:
    if i == "Gray":
        gray += 1
    elif i == "Cinnamon":
        red += 1
    elif i == "Black":
        black += 1

data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count" : [gray, red, black]
}

da_cs = pandas.DataFrame(data_dict)
da_cs.to_csv("Squirrel count")