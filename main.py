# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # temp_data = data["temp"].to_list()
# # temp_average = round((sum(temp_data)) / len(temp_data))
# # print(temp_average)
# # print(data["temp"].max())
# monday = data[data.day == "Monday"]
# # print(monday)
# f_temp = monday.temp * 1.8 + 32
# print(f_temp)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"].tolist()
black = fur_color.count("Black")
cinnamon = fur_color.count("Cinnamon")
gray = fur_color.count("Gray")
data_dict = {
    "fur color": ["Black", "Cinnamon", "Gray"],
    "count": [black, cinnamon, gray],
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("color count")