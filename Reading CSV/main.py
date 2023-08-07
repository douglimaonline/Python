# import pandas as pd
# data = pd.read_csv("weather_data.csv")
# monday = data[data.day == "Monday"]
# print(monday.temp * 9/5 + 32)
import pandas
import pandas as pd
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
cinnamon_count = (len(data[data['Primary Fur Color'] == 'Cinnamon']))
gray_count = (len(data[data['Primary Fur Color'] == 'Gray']))
black_count = (len(data[data['Primary Fur Color'] == 'Black']))

data_dict = {
    'Fur color': ['Cinnamon', 'Gray', 'Black'],
    'Count': [cinnamon_count, gray_count, black_count]
}
dt = pandas.DataFrame(data_dict)
dt.to_csv('squirrel_count.csv')
