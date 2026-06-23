import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Voice Engine
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()

    except:
        return ""

speak("Hello, I am Jarvis. How can I help you?")

while True:

    command = listen()

    if "google" in command:

        speak("Opening Google")

        webbrowser.open("https://www.google.com")

    elif "youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://www.youtube.com")

    elif "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        speak(f"The current time is {current_time}")

    elif "hello" in command:

        speak("Hello, nice to meet you.")

    elif "bye" in command or "exit" in command:

        speak("Goodbye!")

        break

    elif command != "":

        speak("Sorry, I don't understand.")