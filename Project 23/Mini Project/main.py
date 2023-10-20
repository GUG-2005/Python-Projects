# import csv
#
# with open("weather_data.csv") as file:
#     content = csv.reader(file)
#     temperatures = []
#     for i in content:
#         if i[1] != "temp":
#             temperatures.append(int(i[1]))
#     print(temperatures)
import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
maxi = data["temp"].max()

tem = data[data.day == "Monday"]
tem_i = tem.temp[0]
print((tem_i*1.8)+32)