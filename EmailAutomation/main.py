import smtplib
import os
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print("Listening to you ....")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        print("Facing an error right now")


load_dotenv()


def sendEmail(reciever, subject, text):
    EmailAdress = os.environ.get("EMAIL_ID")
    Password = os.environ.get("PASSWORD_EMAIL")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EmailAdress, Password)
    email = EmailMessage()
    email["From"] = EmailAdress
    email["To"] = reciever
    email["Subject"] = subject
    email.set_content(text)
    server.send_message(email)

emails=os.environ.get('EMAIL_LIST')
email_list=eval(emails)

def get_Email_Info():
    talk("To Who do you want to send the Email")
    name = get_info()
    reciever = email_list[name]
    print(reciever)
    talk("What is the Subject of your email")
    subject = get_info()
    talk("What is the Body of your email")
    text = get_info()
    talk("Hey your Email is fast as lightning")
    talk(" Do you want to tire me more or just stay quiet? Answer in Yes or No")
    send_more = get_info()
    sendEmail(reciever, subject, text)
    if "yes" in send_more:
        get_Email_Info

    


get_Email_Info()
