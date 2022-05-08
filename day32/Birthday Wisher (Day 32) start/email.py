import smtplib

my_mail = "dennis.cardoso.122@gmail.com"
password = "ejtrsnsmkfqfgnor"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(from_addr=my_mail,
                        to_addrs="dennis.cardoso@outlook.com", msg="Subject:Hello\n\nThis is the body of my email")
