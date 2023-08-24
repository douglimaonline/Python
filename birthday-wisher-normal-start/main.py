from datetime import datetime
import pandas as pd
import random
import smtplib

date = datetime.now()
today = (date.month, date.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    bday_name = birthdays_dict[today]["name"]
    bday_email = birthdays_dict[today]["email"]
    file_path = f"./letter_templates/letter_{random.choice(range(1, 3))}.txt"
    with open(file_path) as set_letter:
        letter = set_letter.read()
        letter = letter.replace("[NAME]", bday_name)

MY_EMAIL = "douglasbarbozadev@gmail.com"
MY_PASSWORD = "xqitmvsnarwtwvdv"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=bday_email,
                        msg=f"Subject:Happy Birthday\n\n{letter}")
