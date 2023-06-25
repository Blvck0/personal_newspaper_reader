import pyttsx3
import requests

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[1].id)
# print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
    speak('Hello, Welcome to my channel')

    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=6dac729af57e4091ae76f578973e6085"





# 6dac729af57e4091ae76f578973e6085