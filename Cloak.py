///This is a realtime helper///
pip install SpeechRecognition pyttsx3 wikipedia pyaudio
import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize the recognizer and text to speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("You said:", command)
            return command
    except:
        pass
    return ""

def run_alexa():
    command = listen()
    if 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, sentences=2)
        print(info)
        talk(info)
    elif 'how are you' in command:
        talk("I am fine, thank you!")
    elif 'what is your name' in command:
        talk("I am your Python assistant!")
    else:
        talk("Please say the command again.")

while True:
    run_alexa()
