import smtplib
import os
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
import imaplib
import email
import webbrowser
# Creating an Instance of Recognizing Voice
listener = sr.Recognizer()
# Decreasing Mic Sensitivity to make it undersand clearer
listener.energy_threshold=2000
engine = pyttsx3.init()
load_dotenv()
# Getting list of emails
emails=os.environ.get('EMAIL_LIST')
email_list=eval(emails)


#Getting USER email and passwords
EmailAdress = os.environ.get("EMAIL_ID")
Password = os.environ.get("PASSWORD_EMAIL")


#Initializing IMAP for reading mails
con=imaplib.IMAP4_SSL('imap.gmail.com')
con.login(EmailAdress,Password)
con.select('"[Gmail]/All Mail"', 
readonly = True)



# Function to speak out any text passed
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Get Input from the User
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




# Send the mail to with the parameters entered by the User
def sendEmail(reciever, subject, text):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EmailAdress, Password)
    email = EmailMessage()
    email["From"] = EmailAdress
    email["To"] = reciever
    email["Subject"] = subject
    email.set_content(text)
    server.send_message(email)


# Get info from user for the mail that has to be sent
def get_Email_Info():
    talk("To Who do you want to send the Email")
    name = get_info()
    reciever = email_list[name]
    print(reciever)
    talk("What is the Subject of your email")
    subject = get_info()
    talk("What is the Body of your email")
    text = get_info()
    sendEmail(reciever, subject, text)
    talk("Hey your Email is fast as lightning")
    talk(" Do you want to tire me more or just stay quiet? Answer in Yes or No")
    send_more = get_info()
    if "yes" in send_more:
        get_Email_Info


#Getting emails now
def get_mail(con):
    print("Getting mail")
    result,data=con.search(None,'Unseen')
    data= data[0].split()
    latest=int(data[-1])
    for i in range(latest,latest-1,-1):
        res,msg=con.fetch(str(i),"(RFC822)")
        
        for response in msg:
            if isinstance(response,tuple):

                msg=email.message_from_bytes(response[1])
                print(msg["Date"])
                talk("The date is was sent on is")
                talk(msg["Date"])
                print(msg["From"])
                talk("The mail was sent from")
                talk(msg["From"])
                print(msg["Subject"])
                talk("The Subject is")
                talk(msg["Subject"])
                
        for part in msg.walk():
            if part.get_content_type()=="text/plain":

                body=part.get_payload(decode=True)
                talk("The body of the mail is")
                bodyMail=f'Body:{body.decode("UTF-8")}'
                talk(bodyMail)
                print(bodyMail)



def mainFile():
    talk("Please enter your name")
    Name=input("Enter your name here")
    text="Hello {}. Let's check your unread mail".format(Name)
    talk(text)
    get_mail(con)

mainFile()