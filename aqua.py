
import pyttsx3

import datetime  

import speech_recognition as sr

import wikipedia

import webbrowser

import os

import smtplib 

import pyjokes
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
def speak(audio):

       engine.say(audio)

       engine.runAndWait() 

def wishme(): 

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:

        speak("Good morning! jasmeet, I'm Aqua. how do you want me to help you")

    elif hour>=12 and hour<18:

        speak("Good Afternoon! jasmeet, I'm Aqua. how do you want me to help you")    

    else:

        speak("Good evening! Jasmeet singh, I'm Aqua. how do you want me to help you")

 

def takeCommand():



    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        r.pause_threshold = 1

        audio = r.listen(source)

 

    try:

        print("Recognizing...")    

        query = r.recognize_google(audio, language='en-in') 

        print(f"User said: {query}\n")  

 

    except Exception as e:

         #print(e)    

        print("Say that again please...")  

        return "None" 

    return query

 

def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()

    server.starttls()

    server.login('email@gmail.com', 'password')

    server.sendmail('email@gmail.com', to, content)

    server.close()

 

if __name__ == "__main__":

    wishme()

    while True:

   

        query = takeCommand().lower() 

 

        if 'wikipedia' in query:  

            speak('Searching Wikipedia...')

            query = query.replace("wikipedia", "")

            results = wikipedia.summary(query, sentences=2) 

            speak("According to Wikipedia")

            print(results)

            speak(results)

 

        elif 'hello' in query:

            wishme()

 

        elif 'how are you' in query:

            speak("I am fine, Thank you")

            speak("How are you, Sir")

 

        elif 'fine' in query or "good" in query:

            speak("It's good to know that your fine")

 

        elif 'joke' in query:

 

            speak(pyjokes.get_joke())

 

        elif 'open youtube' in query:

            speak("opening youtube")

            webbrowser.open("youtube.com")

            

        elif 'open google' in query:

            speak("opening google")

            webbrowser.open("www.google.com")

        

        elif 'open stack overflow' in query:

            speak("opening stack overflow")

            webbrowser.open("stackoverflow.com")

 

        elif 'about yourself' in query:

            speak("I am Aqua,  a desktop assistant created by group 3 ")

            speak("""I Can help you with handy tasks, like playing some music or 

            telling you the time, and also open different sites for you. I can find locations for you and also 

            send emails""")

 

        elif 'facebook' in query:

            speak("opening facebook")

            webbrowser.open("facebook.com")

 

        elif 'twitter' in query:

            speak("opening twitter")

            webbrowser.open("twitter.com")

 

        elif "where is" in query:

 

            query = query.replace("where is", "")

 

            location = query

 

            speak("User asked to Locate")

 

            speak(location)

 

            webbrowser.open("https://www.google.com/maps/place/" + location + "")

 

        elif 'play music' in query:

            music_dir = 'D:\\Test folderMusic'

            songs = os.listdir(music_dir)

            print(songs)    

            os.startfile(os.path.join(music_dir, songs[0]))

 

        elif 'the time' in query:

            strTime = datetime.datetime.now().strftime("%H:%M:%S")    

            speak(f"Sir, the time is {strTime}")

 

        elif 'open code' in query:

            codePath = "C:\\Users\\lenovo\\Documents\\AQUA\\aqua.py"

            os.startfile(codePath)

 

        elif 'send email' in query:

            try:

                speak("What should I say?")

                content = takeCommand()

                to = "youremail@gmail.com"    

                sendEmail(to, content)

                speak("Email has been sent!")

            except Exception as e:

                print(e)

                speak("Sorry Sir. I am not able to perform this function yet")  

 

        elif 'thank you' in query:

            speak("Im glad, i was able to help you sir")

            break