import smtplib

my_email = "douglasbarbozadev@gmail.com"
password = "xqitmvsnarwtwvdv"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="douglimaonline@gmail.com",
                        msg="Subject:Automatic Hello\n\nMessenger send by python smtplib by douglas_barboza_dev")
