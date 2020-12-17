import smtplib
import datetime as dt
import random
import pandas

my_email = "qazxswqaz04@gmail.com"
my_password = "qetuo123"
s_mail_password = "qetuo123."
name = ""
mail = ""

datas = pandas.read_csv("birthdays.csv")
d_dic = datas.to_dict()
days = datas["day"].tolist()
months = datas["month"].tolist()
names = datas["name"].tolist()
mails = datas["email"].tolist()

now = dt.datetime.now()
day = now.day
month = now.month

l_letter = [r"C:\Users\Lenovo\PycharmProjects\BirthdayWisher\letter_templates\letter_1.txt",
            r"C:\Users\Lenovo\PycharmProjects\BirthdayWisher\letter_templates\letter_2.txt",
            r"C:\Users\Lenovo\PycharmProjects\BirthdayWisher\letter_templates\letter_3.txt"]


def sent_mail():
    letter = random.choice(l_letter)

    with open(letter) as f:
        l = f.read()
        l = l.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=mail,
            msg=f"Subject:Hello\n\n {l}"
        )


for i in range(0, len(days)):
    if days[i] == day and months[i] == month:
        name = names[i]
        mail = mails[i]
        sent_mail()
