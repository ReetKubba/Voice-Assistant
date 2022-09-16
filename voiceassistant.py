import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import datetime
from playsound import playsound
import wikipedia
import pyautogui
Assistant=pyttsx3.init('sapi5')
voices=Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',260)
def Speak(audio):
    print(' ')
    Assistant.say(audio)
    print(' ')
    Assistant.runAndWait()
def takecommand():
    command=sr.Recognizer()
    with sr.Microphone() as source:
        command.adjust_for_ambient_noise(source)
        print('Listening')
        #print(command)
        command.pause_threshold=1
        audio=command.listen(source)
        try:
            print('Recognizing.....')
            query=command.recognize_google(audio,language='en-in')
            print(f"You said :{query}")
        except Exception as Error:
            return "None"
        return query.lower()
def OpenApps():
    Speak("Ok sir, wait a second")
    if 'code' in query: 
        os.startfile(r"C:\Users\dell\AppData\Local\Programs\Microsoft VS Code\Code.exe")
    elif 'chrome' in query:
        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    elif 'facebook' in query:
        webbrowser.open("https://www.facebook.com/")
    elif 'instagram' in query:
        webbrowser.open("https://www.instagram.com/")
    elif 'map' in query:
        webbrowser.open("https://www.google.com/maps/@53.3430272,-6.2554112,13z")

def Whatsapp():
        Speak("Tell Me the phone number of the person you want to send whatsapp message")
        phone=takecommand()
        ph="+91"+"phone"
        Speak("Tell me the message")
        msg=takecommand()
        Speak("Tell me the time sir")
        Speak("Time in hours?")
        hour=int(takecommand())
        
        Speak("Time in minutes?")
        min=int(takecommand())
        
        pywhatkit.sendwhatmsg(ph,msg,hour,min)
        Speak(("Ok sir, Sending whatsapp message"))

while True:
    query=takecommand()
    if 'hello' in query:
        Speak("Hello Sir, I am Jarvis")
        Speak("Your personal AI assistant")
        Speak("How may i help you?")
    elif 'how are you' in query:
        Speak("I am fine sir")
        Speak("What about you?")
    elif 'you need a break' in query:
        Speak("Ok sir , You can completely call me anytime !")
        break
    elif 'bye' in query:
        Speak("Ok Sir, Bye!")
        break
    elif 'youtube search' in query:
        Speak("Ok sir,This is what i found for your search")
        query=query.replace("jarvis","")
        query=query.replace("youtube search","")
        web='https://www.youtube.com/results?search_query='+query
        webbrowser.open(web)
        Speak("Done sir")
    elif 'google search' in query:
        Speak("This is what i found for your search")
        query=query.replace("jarvis","")
        query=query.replace("google search","")
        pywhatkit.search(query)
        Speak("Done sir")
    elif 'website' in query:
        Speak("Ok sir, Launching")
        query=query.replace("jarvis","")
        query=query.replace("website","")
        web1=query.replace("open","")
        web2='https://www.'+web1+'.com'
        webbrowser.open(web2)
        Speak("Launched")
    elif 'wikipedia' in query:
        Speak('Searching wikipedia')
        query=query.replace("Jarvis","")
        query=query.replace("wikipedia","")
        wiki=wikipedia.summary(query,2)
        Speak(f"According to the wikipedia: {wiki}")
    elif 'send whatsapp message' in query:
        Whatsapp()
    elif 'screenshot' in query:
        kk=pyautogui.screenshot()
        kk.save(r"C:\Users\dell\Downloads\jarvisscreenshot.png")
    elif 'open chrome' in query:
        OpenApps()
    elif 'open code' in query:
        OpenApps()
    elif 'open facebook' in query:
        OpenApps()
    elif 'open instagram' in query:
        OpenApps()
    elif 'open map' in query:
        OpenApps()

    elif 'close code' in query:
        os.system("TASKKILL /F /im Code.exe")
    elif 'alarm' in query:
        Speak("Enter the Time")
        time=input("Enter the time")
        while True:
            Time_Ac=datetime.datetime.now()
            now=Time_Ac.strftime("%H:%M:%S")

            if now==time:
                Speak("Time to wake up sir")
                playsound("alarm.mp3")
                Speak("Alarm Closed")
            elif now>time:
                break



      
   