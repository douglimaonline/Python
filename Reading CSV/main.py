import pandas as pd


data = pd.read_csv("weather_data.csv")
monday = data[data.day == "Monday"]
print(monday.temp * 9/5 + 32) 




