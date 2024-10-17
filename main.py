# from ast import While
# import imp
import tkinter as tk

# import pygame
# import pygame.freetype

import pyttsx3
import pyaudio
import pyautogui
import speech_recognition 
import webbrowser
import sounddevice
from pydub.playback import play
from pydub import AudioSegment

def startsound():
    audio=AudioSegment.from_wav("media/start up sound.wav")
    play(audio)

def endsound():
    audio=AudioSegment.from_wav("media/end up sound.wav")
    play(audio)

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("\n Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,3)

    try:
        # print("Understanding..")
        query  = r.recognize_google (audio,language='en-in') # type: ignore
        print(f"{query}\n")
        file=open("myfile.txt",'w')
        file.write(query)
        file.close()

    except Exception as e:
        print("Say that again")
        return "None"
    return query


def loop():
    startsound()
    while True:
                query = takeCommand().lower()

                if "go to sleep" in query or "sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break

                elif "who created you" in query:
                    speak("i was created in lab")
                    break

                # elif "object" in query:
                #     from Object_Detection import dection
                #     dection()
                #     break

                elif "thank you" in query or "thanks" in query:
                    speak("you are welcome")
                    break

                elif "launch" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                    break

                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                    break

                elif "search" in query:
                    from SearchNow import Search_respond_to_query
                    Search_respond_to_query(query)
                    break
                
                elif "play" in query:
                    from SearchNow import play_song
                    play_song(query)
                    break

                elif "tell me about" in query or "what is" in query or "how" in query or "what do" in query or "who is" in query:
                    from SearchNow import respond_to_query
                    respond_to_query(query)
                    break

                elif "shutdown" in query:
                    speak("closing the program")
                    # pygame.quit()
                    exit()
            


if __name__ == "__main__":
    speak("Hello I am Edith")
    startsound()
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()
            endsound()
            while True:
                loop()

        else:
            if "edit" in query:
                speak("waiting for comand") 
                endsound()
                while True:
                    loop()

            elif "shutdown" in query:
                speak("closing the program")
                # pygame.quit()
                exit()   
    











                # elif "pause" in query:
                #     pyautogui.press("k")
                #     speak("video paused")
                # elif "play" in query:
                #     pyautogui.press("k")
                #     speak("video played")
                # elif "mute" in query:
                #     pyautogui.press("m")
                #     speak("video muted")

                # elif "volume up" in query:
                #     from keyboard import volumeup
                #     speak("Turning volume up,sir")
                #     volumeup()
                # elif "volume down" in query:
                #     from keyboard import volumedown
                #     speak("Turning volume down, sir")
                #     volumedown()



