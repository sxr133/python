import smtplib
import datetime as dt
import random

MY_EMAIL = "sterous@gmail.com"
MY_PASSWORD = "jekraqeyxlyhfnwr"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        # makes connection secure
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="sterous@yahoo.com",
                            msg=f"Subject:Daily Motivation\n\n{quote}"
                            )
