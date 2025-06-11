import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import time
import os


recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="facd1c5611004898bd67a12509def606"
def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    # installing gtts as its better than google
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    

#using AI for the code of playing mp3 in pygame
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load and play MP3
    pygame.mixer.music.load('temp.mp3')  # Replace with your file name but here we're using unload so no argu
    pygame.mixer.music.play()

    # Keep the script running until the music finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")
def aiProcess(command):
    #This program was meant to be compatible with chatgpt but api is paid so chatgpt won't help until you get you own api key by paying to open ai
    
    
    client=OpenAI(api_key="<Your own api key here",
    )
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud.Please give short responses."},
        {"role": "user", "content": "command"}
    ]
    )
    return completion.choices[0].message.content



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    if "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    if "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    if "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code==200:
            #this took from AI but can be extracted from loops
            #Parse the json resp
            data=r.json()
            #Extract the articles
            articles=data.get('articles', [])
            #Print the hline
            for article in articles:
                speak(article['title'])
    else:
        #Open will handle
        output= aiProcess(c)
        speak(output)


if  __name__=="__main__":
    speak("Initializing Jarvis...")
    while True:
        #Listen for the wake word Jarvis 
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("Recognizing...")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=4) 
            word =r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio=r.listen(source)
                    command =r.recognize_google(audio)
            
                    processCommand(command)
            
        except Exception as e:
            print("Sphinx error; {0}".format(e))