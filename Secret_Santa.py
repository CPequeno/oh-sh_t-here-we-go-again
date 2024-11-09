import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def Secret_Santa(people, mails, user_smtp, password_smtp):
    friends = people[:]
    
    while True:
        random.shuffle(friends)
        if all(person != friend for person, friend in zip(people, friends)):
            break

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user_smtp, password_smtp)

    for person, friend in zip(people, friends):
        receiver = mails[person]
        message = MIMEMultipart()
        message['From'] = user_smtp
        message['To'] = receiver
        message['Subject'] = "🎅🎄 Secret Santa 🎄🎅" # Here, write the subject of your mail

        main = f"Ho ho ho(la), {person}:\n\nYou are the secret Santa of {friend}.\n\nMerry Christmas!"
        # Here, write the body of your mail. Only edit the text without brackets, {person} and {friend} is what the program generates randomly.
        message.attach(MIMEText(main, 'plain'))
        
        server.sendmail(user_smtp, receiver, message.as_string())

    server.quit()

people = ["X", "Y", "Z"]
mails = {
    "X": "X@gmail.com",
    "Y": "Y@gmail.com",
    "Z": "Z@gmail.com"
}

user_smtp = "X@gmail.com"
password_smtp = "" # You need to use an app password. You can generate one for "Mail" in "https://myaccount.google.com/apppasswords". 

Secret_Santa(people, mails, user_smtp, password_smtp)