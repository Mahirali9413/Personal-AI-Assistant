import speech_recognition as sr
from time import ctime
import time, datetime
import random as rn
import face_recognition as fr
import cv2
import pandas as pd
import ast, pyttsx3
from csv import writer
import sys
import requests
import bs4
from bs4 import BeautifulSoup
import smtplib
import wikipedia
import webbrowser

csvdata=pd.read_csv(r'convo.csv')
print(csvdata)

ch=['ans1','ans2','ans3']
df = pd.DataFrame([[0,0]], columns = ['name','encoding'])
df=pd.read_csv(r'asd2.csv')
print(df)

def pspeak(squery):
        print(squery)
        pyttsx3.speak(squery)

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
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
        pspeak("good morning")
    elif hour>12 and hour<18:
        pspeak("good afternoon")
    else:
        pspeak("good evening")
    pspeak("Hello i am aprajita's Jarvis How may i help you" )
    
def wishme_end():
    pspeak("bye bye signing off, thanks for using")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        pspeak("Good Morning")
    elif (hour >= 12 and hour < 18):
        pspeak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        pspeak("Good Evening")
    else:
        pspeak("Goodnight.. Sweet dreams")
    quit()



def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    pspeak("The current date is")
    pspeak(date)
    pspeak(month)
    pspeak(year)

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mahirali9413@gmail.com', '9413645115')
    server.sendmail('mahirali9413@gmail.com', to, content)
    server.close()

def personal():
    pspeak("I am mahir's personal assisstant")
    pspeak("Now i hope you know me")
    
def developer():
    pspeak("I am developed by mister mahir ali in 23rd may 2021")

def aboutyou():
    pspeak("I am good , what about you sir?")
    pspeak("ok cool, how may i help you")

def face_recognition():
        v=cv2.VideoCapture(0)
        kfe=[]
        for i in range(len(df['encoding'])):
            res = ast.literal_eval(df['encoding'][i])
            kfe.append(res)
        #kfe.remove(0)
        #pspeak(kfe)
        name=list(df['name'])
        #name.remove('0')
        print('list of names in database\n      ',name)

        while(1):
            r,limg=v.read()
            img=cv2.resize(limg,(0,0),fx=0.25,fy=0.25)
            face=fr.face_locations(img)
            if(len(face)>0):
                imge=fr.face_encodings(img)[0]
                r=fr.compare_faces(kfe,imge)
                print('person in the database',r)
                if True in r:
                    ind=r.index(True)
                    print('index of the person in the database: ',ind)
                    pspeak('Hello '+ name[ind]+', Nice to Meet You.')
                    break
                else:
                    pspeak("You are welcome, you are new to me, what is your name?")
                    new_name = input('what is your name, please type: ')
                    list1=[len(df['encoding']),new_name,list(imge)]
                    
                    with open('asd2.csv', 'a') as f_object:
                        writer_object = writer(f_object)
                        writer_object.writerow(list1)
                        f_object.close()
                    break

            cv2.imshow('face_recognition',img)
            k=cv2.waitKey(1)
            if(k==ord('q')):
                break
        cv2.destroyAllWindows()
        v.release()


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        pspeak("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        data =data.lower()
        print("You said: " + data)
    except sr.UnknownValueError:
        pspeak("I could not understand audio")
        data ="*"
    except sr.RequestError as e:
        pspeak("Could not request results from Google Speech Recognition service; {0}".format(e))
        data ="*"
    return data

def jarvis(query):
        if "thank you" in query or "bye bye" in query:
                pspeak('Thank you for visiting')
                return 0

        elif ("wikipedia" in query):
                pspeak("searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                pspeak(query)
                pspeak(result)

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
            
        elif ("open youtube" in query):
                 webbrowser.open("YouTube.com") 
            
        elif ("open google" in query):
                pspeak("sir,what would i search on google")
                cm=takecommand().lower()
                webbrowser.open(f"{cm}")

        elif ("the time" in query):
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                pspeak(f"sir, the timeis{strTime}")

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

        elif "weather in " in query:
                query=query.replace('weather in ','')
                search='weather in '+query
                url=f"https://www.google.com/search?q={search}"    
                r=requests.get(url)  
                data=BeautifulSoup(r.text,"html.parser")
                weather=data.find("div",class_="BNeawe").text
                pspeak(f"current {search} is {weather}")

        elif ("send email" in query):
            try:
                pspeak("What is the message for the email")
                content=takecommand()
                to = 'traptid11@gmail.com'
                sendemail(to, content)
                pspeak("Email has sent")
            except Exception as e:
                pspeak(e)
                pspeak("Unable to send email check the address of the recipient")


        elif ('i am done' in query or 'bye bye jarvis' in query or 'go offline jarvis' in query or 'bye' in query or 'nothing' in query):
                 wishme_end()
        else:
                try:
                    cd = csvdata["ques"] == query
                    di=csvdata.index
                    dw = di[cd]
                    if(len(dw)>0):
                        while(1):
                            pdata=csvdata[rn.choice(ch)][dw[0]]
                            if(str(pdata)=='nan'):
                                continue
                            else:
                                break
                    pspeak(pdata)
                except:
                    pspeak('Sorry, can you speak again')
        return 1


# initialization
q=1
face_recognition()
while(q):
        data = recordAudio()
        #data =input("Enter command: ")
        if(data=="*"):
                continue
        else:
                q=jarvis(data)

