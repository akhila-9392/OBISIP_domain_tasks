import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I didn't understand.")
        return ""

speak("Hello! I am your voice assistant")

while True:
    command = listen()

    if "hello" in command:
        speak("Hello Akhila! How can I help you?")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)

    elif "search" in command:
        speak("What should I search?")
        query = listen()
        webbrowser.open("https://www.google.com/search?q=" + query)
        speak("Here are the results for " + query)

    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 2)
        speak(info)

    elif "exit" in command:
        speak("Goodbye Akhila")
        break