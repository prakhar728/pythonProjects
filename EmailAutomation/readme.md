## EMAIL AUTOMATION
This is a simple Email Automation Program

The program flow goes like this
1. First it asks the name of the person you want to send to
2. Recognizes the name and uses the Email associated with it
3. It asks the Subject of Email
4. Recognizes the subject that is to be used
5. Asks for the body of the email
6. Recognizes the Body of the mail
7.  Sends out the mail and prompts if you want to send another mail

## DEPENDENCIES USED
The packages used in the script are - 
1. smtplib - For sending Email
2. dotenv - For usng environment Variables
3. SpeechRecognition - For recognizing voice commands
4. pyttsx3 - Text to Speech conversion
5. pyaudio 
6. Default python Email library

## USING ENV FILE
1. Create ENV file 
2. Add Email to be used as *EMAIL_ID ="examplemail@gmail.com"*
3. Add Password to be used as *PASSWORD_EMAIL="passwordisthis"*
4. Add List of emails as python dictonaries
  >EMAIL_LIST='{"name":"Emailassociated@gmail.com" , "name1":"Emailassociated@gmail.com}'



