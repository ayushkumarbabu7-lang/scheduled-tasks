##################### Extra Hard Starting Project ######################
import  datetime as dt
import random
import smtplib
import pandas
my_email = "ayushkumarbabu5@gmail.com"
password = "itet emxf tzmv kpvv"
now = dt.datetime.now().strftime("%d-%m")
dataframe = pandas.read_csv("birthdays.csv")
letters = ["letter_templates/letter_3.txt","letter_templates/letter_2.txt","letter_templates/letter_1.txt"]
for e in dataframe["name"] :
    row = dataframe[dataframe["name"] == e]
    date = dt.datetime(year=row.year.iloc[0], month=row.month.iloc[0], day=row.day.iloc[0]).strftime("%d-%m")
    if now == date :
        randomletter = random.choice(letters)
        name = row.name.iloc[0]
        with open(randomletter,mode ="r") as letter :
            letterc = letter.read()
        letterc = letterc.replace("[NAME]",e)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=row.email.iloc[0],
                            msg= f"subject:HAPPY BIRTHDAY \n  \n {letterc}")
    print("hello")



