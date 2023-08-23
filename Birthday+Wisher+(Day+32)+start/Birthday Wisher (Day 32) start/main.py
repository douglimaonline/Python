import smtplib

my_email = "douglasbarbozadev@gmail.com"
password = "xqitmvsnarwtwvdv"

connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="lima_on-line@hotmail.com", msg="Hello")
connection.close()
