import csv
import pandas as pd
from statistics import mean
pd.set_option('display.max_columns', None)

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_dict = {"Fur Color": [],
                 "Count": []}

for color in ["Gray", "Cinnamon", "Black"]:
    squirrel_color_data = squirrel_data[squirrel_data["Primary Fur Color"] == color]
    squirrel_color_count = len(squirrel_color_data.index)
    squirrel_dict["Fur Color"].append(color)
    squirrel_dict["Count"].append(squirrel_color_count)

print(squirrel_dict)
data = pd.DataFrame(squirrel_dict)
data.to_csv("squirrel_count.csv")

