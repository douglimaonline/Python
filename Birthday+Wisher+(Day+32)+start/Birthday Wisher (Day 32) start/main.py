import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:

    MY_EMAIL = "douglasbarbozadev@gmail.com"
    PASSWORD = "xqitmvsnarwtwvdv"

    with open("quotes.txt") as quotes:
        all_quotes = [quote for quote in quotes]
        random_quote = random.choice(all_quotes)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="douglimaonline@gmail.com",
                            msg=f"Subject:Your Motivation today\n\n{random_quote}")
