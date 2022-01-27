
import webbrowser # module to open web browsers after taking input from the user
import os
import smtplib # module required for sending emails
import random
import wikipedia #module required to fetch data from the wikipedia
import pyttsx3 #module fot text to speech conversion
import speech_recognition as sr #pip install speechRecognition
import datetime  # module used to extract the date and time data
import pywhatkit









assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
# print(voices[1].id)
assistant.setProperty('voice', voices[1].id)


def say(audio):  # function to speak
    assistant.say(audio)
    assistant.runAndWait()


def Wish_user():  # Function to wish user according to time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say("Good Morning!")

    elif hour>=12 and hour<18:
        say("Good Afternoon!")   

    else:
        say("Good Evening!")  

    say("I am Lucifer.. your  AI assistant . Please tell me how may I help you")       

def takeCommand():  #Function to take microphone input from the user and return string output
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #using google to recognize the given command with specified language
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print(" Can you Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls() #Standard TLS encryption
    server.login('gauravgamessoftwares@gmail.com', 'gaurav472002')
    server.sendmail('gauravgamessoftwares@gmail.com', to, content)
    server.close()

def sendmessage(numberwp,messagewp): # function to send whatsapp message
    

    # a1= actTime.split(" ")
    # hours=int(a1[0])
    # minutes=int(a1[1])
    # minutes+=2
    pywhatkit.sendwhatmsg_instantly(numberwp,messagewp)
    

if __name__ == "__main__":
    Wish_user()
    while True:
        
   
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            say('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            say("According to Wikipedia")
            print(results)
            say(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        
        elif 'cooking' in query:
            webbrowser.open("youtube.com/watch?v=JGZolkleYiA")   


        elif 'play music' in query:
            music_dir = 'E:\\Programming---Codes\\Python Projects\\Voice Assistant-     LUCIFER\\song'
            songs = os.listdir(music_dir)
            # print(songs)    
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif ' arijit' in query:
            music_dir1 = 'E:\\Programming---Codes\\Python Projects\\Voice Assistant-     LUCIFER\\song\\Arijit_Singh'
            songs1 = os.listdir(music_dir1)
            # print(songs)    
            os.startfile(os.path.join(music_dir1, random.choice(songs1)))


        elif ' yoyo' in query:
            music_dir2 = 'E:\\Programming---Codes\\Python Projects\\Voice Assistant-     LUCIFER\\song\\YOYO_Honey_Singh'
            songs2 = os.listdir(music_dir2)
            # print(songs)    
            os.startfile(os.path.join(music_dir2, random.choice(songs2)))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            say(f"Sir, the time is {strTime}")

        elif 'open vscode' in query:
            codePath = "C:\\Users\\Gaurav_472\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            

        
        elif 'thank you' in  query:
            say("Your most welcome sir")

       
           

            

        elif 'send email' in query:
            try:
                say("What should I say?")
                content = takeCommand()
                to = "gauravchakraborty472@gmail.com"    #enter sender's email here
                sendEmail(to, content)
                say("Email has been sent! successfully")
            except Exception as e:
                print(e)
                say(" I am not able to send this email really Sorry sir")  
        
        elif 'shutdown' in query:
            say("goodbye sir")
            exit()
            

        elif ' message' in query:
            try:
                say("phone number please")
                ph=takeCommand()
                phnumber="+91"+ph
                print(phnumber)
            
                say("what should I say?")
                textmessage=takeCommand()
                sendmessage(phnumber,textmessage)
            
            except Exception as e:
                say("sorry your message was not sent ")

       
            
            

        