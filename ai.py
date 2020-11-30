import os
import pyttsx3
import smtplib, ssl
import datetime
from datetime import date
import webbrowser 
import speech_recognition as sr
import wikipedia
current_time = datetime.datetime.now() 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "senderemailaddress@gmail.com"
receiver_email="youreamiladdress@gmail.com"
password = "yourpassword"
context = ssl.create_default_context()
menu= '''What i can do :-
🤖I can search anything on wikipedia 
🤖I can Open youtube for you 
🤖I can Open google for you
🤖I can Open github for you
🤖I can Open android studio for you
🤖I can Open Visual studio code for you 
🤖I can tell the current date 
🤖I can even send Emails to your friends 

Sky is the limit,add some code make me more advance 
'''
commands= '''What i can do :-
💁Your search + on wikipedia 
💁Open youtube
💁Open google
💁Open github 
💁Open android studio 
💁Open code
💁what is the date today 
💁send email
💁Exit to quit
Sky is the limit,add some code make me more advance 
'''

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def listen():
    print("I am listening 🎧")
    r = sr.Recognizer()
    r.pause_threshold=1
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)
    try:
        response=r.recognize_google(audio)
        print("User said:🎤"+response)
    except Exception as e:
        print(e)
        print("Please come again 😕")
    return response

def wishMe():
    if 0<= current_time.hour<12:
        speak("Good Morning Sir ")
    if 12<= current_time.hour<=15:
        speak("Good Afternoon Sir")
    if 15<= current_time.hour<=20:
        speak("Good Evening Sir")
    if 20<= current_time.hour<=24:
        speak("Good Night Sir")
    speak("I am jarvis the robot")
    speak("How can I help you")

def sendEmail(content,to):
    pass

    
if __name__ == '__main__':
    wishMe()
    print("➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️")
    print(menu)
    print("➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️")
    print(commands)
    print("➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️➡️")
    while True:
        query =listen().lower()
        if "wikipedia" in query:
            actual_query=query.replace('wikipedia','')
            result=wikipedia.summary(actual_query, sentences=2)
            speak("Searching on wikipedia")
            print(result)
            speak(result)
        elif "open google" in query:
            webbrowser.open('http://www.google.com')
            print("Done ✅")

        elif "open github" in query:
            webbrowser.open('https://github.com/') 
            print("Done ✅")

        elif "open youtube" in query:
            webbrowser.open('https://www.youtube.com/') 
            print("Done ✅")
        
        elif "open android studio" in query:
            path="/Users/vijaykumar/Desktop/Android\ Studio.app"
            os.system(f"open {path}")
            print("Done ✅")
        
        elif "open code" in query:
            path="/Users/vijaykumar/Downloads/Visual\ Studio\ Code.app"
            os.system(f"open {path}")
            print("Done ✅")

        elif "date today" in query:
            today = date.today()
            d1 = today.strftime("%B %d, %Y")
            print(d1)
            speak(d1)
        elif "send email" in query:
            speak("what should i say")
            content=listen()
            try:
                server = smtplib.SMTP(smtp_server,port)
                server.ehlo() # Can be omitted
                server.starttls(context=context) # Secure the connection
                server.ehlo() # Can be omitted
                server.login(sender_email, password)
                server.sendmail(sender_email,receiver_email,content)
                print("Email sent 😊")
                # TODO: Send email here
            except Exception as e:
                # Print any error messages to stdout
                print(e)
        elif "quit" in query:
            print("👋👋👋👋👋👋👋")
            speak("Good by Sir")
            break
            


           
        
        
        
            




