import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
#print(voices[0])
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<=12):
        speak("Good Morning!")
    elif(hour>=12 and hour<17):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How may I help you")

def takeCommand():
    """
    Takes microphone input from user and returns string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #r.energy_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please!")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shan.roy1999@gmail.com','Ronaldo@71999')
    server.sendmail("shan.roy1999@gmail.com", to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            print("Searching Wikipedia....")
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            r2 = sr.Recognizer()
            url = "https://www.youtube.com/results?search_query="
            with sr.Microphone() as source:
                speak("Which video do you want to watch?")
                audio = r2.listen(source)

                try:
                    get = r2.recognize_google(audio)
                    print(get)
                    wb.get().open_new(url + get)

                except sr.UnknownValueError:
                    print("Error")

                except sr.RequestError as e:
                    print("failed".format(e))
                    
        elif "search" in query:
            r3 = sr.Recognizer()
            url = "https://www.google.com/search?q="
            with sr.Microphone() as source:
                speak("What would you like to search for?")
                audio = r3.listen(source)

                try:
                    get = r3.recognize_google(audio)
                    print(get)
                    wb.get().open_new(url + get)

                except sr.UnknownValueError:
                    print("Error")

                except sr.RequestError as e:
                    print("failed".format(e))
        
        elif "find location" in query:
            r4 = sr.Recognizer()
            url = "https://google.nl/maps/place/"
            with sr.Microphone() as source:
                speak("Which location would you like to search for?")
                audio = r4.listen(source)

                try:
                    get = r4.recognize_google(audio)
                    print(get)
                    wb.get().open_new(url + get + '/&amp;')

                except sr.UnknownValueError:
                    print("Error")

                except sr.RequestError as e:
                    print("failed".format(e))


        elif "open google" in query:
            wb.open("google.com")

        elif "open stackoverflow" in query:
            wb.open("stackoverflow.com")

        elif "play music" in query:
            wb.open("spotify.com")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "chrome" in query:
            chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(chrome_path)

        elif "email to shantanu" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sb2282@srmist.edu.in"
                sendEmail(to, content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry! I am not able to send email!")

        elif "bye" in query:
            try:
                speak("Goodbye! Nice Talking to You")
                break
            except Exception as e:
                print(e)
