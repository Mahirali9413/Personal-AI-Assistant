from numpy.core.fromnumeric import searchsorted
import pyttsx3
import speech_recognition as SR
import os
import datetime
import cv2
import wikipedia
import webbrowser
import random
import sys
import requests
import bs4
from bs4 import BeautifulSoup
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=SR.Recognizer()
    with SR.Microphone() as source:
        print("listening..")
        r.pause_threshold=1
        audio = r.listen(source,timeout=30,phrase_time_limit=5)  

    try:
        print("Recognizing..")
        query=r.recognize_google(audio, language='en-in')    
        print(f"user said:{query}")
    
    except Exception as e:
        speak("say that again please..")
        return "none" 
    query=query.lower()
    return query

def wish():
    hour = int(datetime.datetime.now().hour)   

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("Hello i am aprajita's Jarvis How may i help you" )
    
def wishme_end():
    speak("bye bye signing off, thanks for using")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()



def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aprajita.lnb@gmail.com', '7991248888')
    server.sendmail('aprajita.lnb@gmail.com', to, content)
    server.close()

def personal():
    speak("I am Aprajita's personal assisstant")
    speak("Now i hope you know me")
    
def developer():
    speak("I am developed by miss aprajita dwivedi in 23rd may 2021")

def aboutyou():
    speak("I am good , what about you mam?")
    speak("ok cool, how may i help you")
     


def TaskExecution():
     wish()
     while True:
     #if 1:
         query = takecommand().lower()
         
         if ("open camera" in query):
            cap = cv2.VideoCapture(0)
            while True:
                 ret,img = cap.read()
                 cv2.imshow('webcam', img)
                 k = cv2.waitKey(50)
                 if k==27:
                   break
            cap.release()
            cv2.destroyAllWindows()

            

         elif ("wikipedia" in query):
            speak("searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(query)
            print(result)
            speak(result)

         elif ("tell me about yourself" in query):
            personal()
         elif ("about you" in query):
            personal()
         elif ("who are you" in query):
            personal()    
         
         elif ("who is aprajita" in query):
             developer()

         elif ("who is your developer" in query):
             developer()    

         elif ("how are you jarvis?" in query):
             aboutyou()
            
         elif ("open YouTube" in query):
             webbrowser.open("YouTube.com") 
             
         elif ("open google" in query):
             speak("mam,what would i search on google")
             cm=takecommand().lower()
             webbrowser.open(f"{cm}")

         elif ("the time" in query):
             strTime=datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Mam, the timeis{strTime}")

         elif ('date' in query):
            date()
        

         elif ("open notepad" in query):
             npath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Notepad++"
             os.startfile(npath)

         elif ("open code" in query):
             npath="C:\\Users\\apraj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(npath)

         elif ("open command prompt" in query):
             os.system("start cmd")

         elif ("open slack" in query):
             npath="C:\\Users\\apraj\\AppData\\Local\\slack\\slack.exe"
             os.startfile(npath) 

         elif ("play music" in query):
             music_dir="C:\\Users\\apraj\\Music" 
             songs=os.listdir(music_dir) 
             rd=random.choice(songs)
             os.startfile(os.path.join(music_dir, rd))

         elif "shutdown" in query:
             os.system('shutdown /s /t 1')
             
         elif "restart" in query:
             os.system('shutdown /r /t 1')
           
         elif "logout" in query:
             os.system('logout -1')

         elif "weather in jaipur" in query:
             search="weather in jaipur"
             url=f"https://www.google.com/search?q={search}"    
             r=requests.get(url)  
             data=BeautifulSoup(r.text,"html.parser")  
             weather=data.find("div",class_="BNeawe").text
             speak(f"current {search} is {weather}")

         elif ("send email" in query):
            try:
                speak("What is the message for the email")
                content=takecommand()
                to = 'traptid11@gmail.com'
                sendemail(to, content)
                speak("Email has sent")
            except Exception as e:
                print(e)
                speak(
                    "Unable to send email check the address of the recipient")


         elif ('i am done' in query or 'bye bye jarvis' in query
              or 'go offline jarvis' in query or 'bye' in query
              or 'nothing' in query):
            wishme_end()

                

         
if __name__ == "__main__":
    while (True):
        permission=takecommand()
        if "wake up" in permission:
          TaskExecution()
        elif 'jarvis quit' in permission or 'exit' in permission or 'close' in permission:
            speak("Thanks you for using Jarvis Mam")
            exit()         

        



             

         





             
         
              
        
            
             
