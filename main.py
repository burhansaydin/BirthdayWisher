import smtplib

my_email = "qazxsw123@gmail.com"
my_password = "qazxsw123"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="qwerasdf123@yahoo.com",
                        msg="Subject:Hello\n\n This is the body of my mail. ")