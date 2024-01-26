import speech_recognition as sr
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone as source:
        pause_threshold = 0.1;
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            print("Recognizing...")
            print(f"User Said: {query}")
            return query
        except Exception as e:
            print("Something Went Wrong")

while True:
    
    speaker.Speak("HEllo sir")