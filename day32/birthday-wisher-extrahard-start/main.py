##################### Extra Hard Starting Project ######################
#Import libraries
import datetime as dt
import random
import smtplib 

# Email credentials
my_mail = "dennis.cardoso.122@gmail.com"
password = "ejtrsnsmkfqfgnor"

# 1. Update the birthdays.csv
contactList = {}
with open("birthdays.csv") as f:
    # adding row into list as strings
    birthdays = f.read().splitlines() 

    #create a list with sublist of itens
    listPeople = []
    for people in birthdays:
        name,email,year,month,day = people.split(",")
        listPeople.append((name,email,year,month,day))

    del listPeople[0]
# 2. Check if today matches a birthday in the birthdays.csv
birthdaysList = []
today = dt.datetime.today()

# Run into the list to get the list value of birthday people
for person in listPeople:
    if (int(person[3]) == int(today.month)) and (int(person[4]) == int(today.day)):
        birthdaysList.append(person)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if birthdaysList:
    for person in birthdaysList:

        # Choose randomly a letter for the user
        lettername = 'letter_{}.txt'.format(random.randint(1,3))
    
        # Read in the letter content
        with open('letter_templates/{}'.format(lettername), 'r') as file :
            bdmessage = file.read()

        # Replace the name for the birthday person
        bdmessage = bdmessage.replace('[NAME]', person[0])

        # 4. Send the letter generated in step 3 to that person's email address.
        # Use the smtplib to send the email to yourself

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail,
                                to_addrs="dennis.cardoso@outlook.com", msg='Subject:Happy Birthday, {}!\n\n{}'.format(person[0],bdmessage))