import pyttsx3 as p
import speech_recognition as sr

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Hello there, My name is Becky. I am your voice assistant")

engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening:")    
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
