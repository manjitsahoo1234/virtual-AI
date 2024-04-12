import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import requests
from bs4 import BeautifulSoup
import pyautogui
import os
import time
import sys
import webbrowser


machine= pyttsx3.init()
def talk(text):
    machine.say(text)
    machine.runAndWait()

def welcome():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        print("Good morning boss")
        talk("Good morning boss")
    elif hour>=12 and hour<17:
        print("Good afternoon boss")
        talk("Good afternoon boss")
    elif hour>17 and hour<21:
        print("Good evening boss")
        talk("Good evening boss")
    else:
        print("Good night boss")
        talk("Good night boss")

welcome()
talk("Good to see you.")
talk("How can I help you")
def input_instruction():
    global instruction
    listener= sr.Recognizer()
    with sr.Microphone() as origin: 
        print("Listening..")
        listener.pause_threshold=1
        speech= listener.listen(origin)
    try:
        print("Recoginzing..")
        instruction= listener.recognize_google(speech,language='en-in')
        print(f"User said: {instruction}\n")

    except Exception as e:
        print("Sorry please repeat..")
        return "None"
    return instruction


if __name__ =="__main__":
    while True:
        instruction= input_instruction().lower()
        if "play" in instruction:
            song= instruction.replace("play","")
            talk("playing"+ song)
            pywhatkit.playonyt(song)
        elif "time" in instruction:
            time= datetime.datetime.now().strftime("%I %M %p")
            print(time)
            talk("current time"+ time)
        elif "date" in instruction:
            date=datetime.datetime.now().strftime("%d / %m / %y")
            print(date)
            talk("Today's date"+ date)   
        elif "movie folder" in instruction:
            os.startfile('E:\movies')
        elif "open" in instruction:
            instruction=instruction.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(instruction)
            time.sleep(1)
            pyautogui.press("enter")
        
        elif "gmail" in instruction:
            pyautogui.moveTo(1130,154)
            time.sleep(2)
            pyautogui.click()
        elif "youtube" in instruction:
            pyautogui.moveTo(160,160)
            pyautogui.click()

        elif "close" in instruction:
            pyautogui.hotkey('alt', 'F4')

        elif "maximize this window" in instruction:
            pyautogui.hotkey('alt','space')
            time.sleep(1)
            pyautogui.press("x")
    
        elif "search" in instruction:
            instruction=instruction.replace("search","")
            pyautogui.hotkey('alt','d')
            pyautogui.write(instruction)
            pyautogui.press("enter")        
            
        elif "how are you" in instruction:
            talk("I am fine, how about you")
        elif "what is your name" in instruction:
            talk("I am sonu, what can I do for you")
        elif "who is" in instruction:
            human=instruction.replace("who is"," ")
            info= wikipedia.summary(human,1)
            print(info)
            talk(info)
        elif "weather" in instruction:
            search=instruction
            url= f"https://www.google.com/search?q={search}"
            w=requests.get(url)
            data=BeautifulSoup(w.text,"html.parser")
            oupt=data.find("div",class_="BNeawe").text
            print(oupt)
            talk(f"current {search} is {oupt}")
        elif "ok bye" in instruction:
            talk("Thank you, have a good day")
            sys.exit()
input_instruction()
