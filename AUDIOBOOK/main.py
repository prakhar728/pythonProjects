import pyttsx3
import PyPDF2

book = open('books.pdf','rb')
pdfReader =  PyPDF2.PdfFileReader(book)
pages= pdfReader.numPages

speaker = pyttsx3.init()
for i in range(pages):
    page = pdfReader.getPage(i)
    text= page.extractText()
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate',rate+100)
    speaker.say(text)
    speaker.runAndWait() 
  

