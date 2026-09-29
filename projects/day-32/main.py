import pandas as pd

# # print(pd.__version__)
# data = [100, 200, 300 , 400, 500]
#
# series = pd.Series(data)
#
# print(type(series.iloc[1]))
#
# print(series.iloc[1])

dict = {
    "student" : ["raj" , "ram" , "sham"],
    "score": [50 , 51, 52]

}
# print(dict)
df = pd.DataFrame(dict)
# print(df)
# print(df["student"])
# print(df.items())

for (key,value) in df.iterrows():
    print(type(value))

