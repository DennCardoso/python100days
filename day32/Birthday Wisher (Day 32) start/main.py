from datetime import datetime as dt
import random as rd
import smtplib

# Get from datetime from datetime function the current day of the week
weekday = dt.today().weekday()

# Open quotes.txt and create a list of motivation messages
with open("day32/Birthday Wisher (Day 32) start/quotes.txt", "r") as line:
    quotes = line.read().splitlines()

# Use Random module to pick a random quote from your list of quotes
niceQuote = rd.choice(quotes)

# Use the smtplib to send the email to yourself
my_mail = "dennis.cardoso.122@gmail.com"
password = "ejtrsnsmkfqfgnor"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(from_addr=my_mail,
                        to_addrs="dennis.cardoso@outlook.com", msg='Subject:Motivational Quotes of the day\n\n{}'.format(niceQuote))
