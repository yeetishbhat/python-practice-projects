
# import csv
import pandas as pd

# # temprature = []
# # with open("weather_data - Sheet1.csv", "r") as f:
# #     # data = f.readlines()
# #     data = csv.reader(f)
#
# data = pd.read_csv('weather_data - Sheet1.csv')
#
# data_dict = data.to_dict()
# print (data_dict)
#
# average = data["temp"].mean()
# print (average)
# maximum = data["temp"].max()
# print (maximum)
# # print (temp_list)
# # total =0
# # for temp in temp_list:
# #     total += temp
# # print (total)
# # average = total / len(temp_list)
# # print(average)
#
# print(data[data.temp == data.temp.max()])


df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

lenght_gray_squ =len(df[df["Primary Fur Color"] == "Gray"])
lenght_red_squ =len(df[df["Primary Fur Color"] == "Cinnamon"])
lenght_black_squ =len(df[df["Primary Fur Color"] == "Black"])

print(lenght_gray_squ)
print(lenght_red_squ)
print(lenght_black_squ)

data_dict = {
    "fur-colour" : ["gray","cinnamon","black"],
    "count":[lenght_gray_squ,lenght_red_squ,lenght_black_squ]
}

df1= pd.DataFrame(data_dict)
df1.to_csv("squ count.csv")




