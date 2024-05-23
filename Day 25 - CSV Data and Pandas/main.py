import csv
import pandas
from statistics import mean




with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

#print(temperatures)

data = pandas.read_csv("weather_data.csv")


data_dict = data.to_dict()
print(data_dict)

temp_max = data["temp"].max()
print(temp_max)

#Get Data in Row
print(data[data['temp'] == temp_max])

monday = data[data['day'] == 'Monday']
print(int(monday['temp']) * 9/5 + 32)

data_dict = {
    "students" : ["Amy", "Sarah", "James"],
    "score" : ["75", "50", "101"]

}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")