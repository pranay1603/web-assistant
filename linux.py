import os
import pyttsx3
import speech_recognition as sr
import time as t


engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
time = int(t.strftime("%H"))
if 5 <= time < 12:
    engine.say("Good Morning")
    engine.runAndWait()
elif 12 <= time < 18:
    engine.say("Good Afternoon")
    engine.runAndWait()
elif 18 <= time < 24 or 0 <= time < 5:
    engine.say("Good Evening")
    engine.runAndWait()
engine.say("hey i am your webpage assistant")
engine.say(" how can i help you")
engine.runAndWait()

while True:
    def speech():
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("start saying...")
                audio = r.listen(source)
                print("\nwait processing your input")
                data = r.recognize_google(audio).lower()
            return data
        except:
            engine.say("sorry repeat again")
            engine.runAndWait()


    s = speech()
    print("\n"+ s)
    if "exit" in s or "quit" in s:
        engine.setProperty("rate", 200)
        engine.say("I am closing the service have a good day")
        engine.runAndWait()
        exit()

    elif "linux command" in s:
        engine.say("I am opening  linux webapp")
        engine.runAndWait()
        os.system("chrome http://192.168.43.155/linux.html")
    elif "start docker container" in s:
        engine.say("I am opening your webapp of docker")
        engine.runAndWait()
        os.system("chrome http://192.168.43.155/start.html")
    elif "stop docker container" in s:
        engine.say("I am opening your webapp of docker")
        engine.runAndWait()
        os.system("chrome http://192.168.43.155/stop.html")
    elif "status of docker container" in s:
        engine.say("I am opening your webapp of docker")
        engine.runAndWait()
        os.system("chrome http://192.168.43.155/status.html")
    elif "docker image" in s:
        engine.say("I am opening your webapp of docker")
        engine.runAndWait()
        os.system("chrome http://192.168.43.155/pull.html")




