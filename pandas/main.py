from datetime import datetime
import pandas as pd


date = datetime.now()
today = (date.month, date.day)

data = pd.read_csv("birthdays.csv")
data_dict = {(row.month, row.day): row.email for (index, row) in data.iterrows()}

if today in data_dict:
    print("ok")