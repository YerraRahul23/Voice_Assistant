# from os import link
import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

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
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,3)

    try:
        # print("Understanding..")
        query  = r.recognize_google(audio,language='en-in') # type: ignore
        print(f"{query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

query = takeCommand()

def Search_respond_to_query(query):
    """Respond to the user's query using Wikipedia or perform searches."""
    search_query = query.replace("search", "")
    
    if "google" in search_query:
        search_query = search_query.replace("google", "").replace("on", "").strip()
        print("Searching......")
        speak(f"Searching for {search_query} on Google.")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
            
def play_song(query):
    search_query = query.replace("play", "")

    if "youtube" in search_query:
        search_query = search_query.replace("youtube", "").replace("on", "").strip()
        print("Searching......")
        speak(f"playing {search_query} on YouTube.")
        web_link = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web_link)
        pywhatkit.playonyt(query) # type: ignore


def respond_to_query(query):
        query=query.replace("ai","AI")

        if "tell me about" in query:
            search_query = query.replace("tell", "").replace("me", "").replace("about", "").strip()
            try:
                print("hello") 
                print(search_query)
                summary = wikipedia.summary(query, sentences=2)
                print(summary)
                speak(summary)
            except Exception as e:
                speak(f"An error occurred: {e}")

        elif "what is" in query:
            search_query = query.replace("what", "").replace("is", "").strip()
            try:
                print("hello") 
                print(search_query)
                summary = wikipedia.summary(query, sentences=2)
                print(summary)
                speak(summary)
            except Exception as e:
                speak(f"An error occurred: {e}")

        elif "how do" in query:
            search_query = query.replace("how", "").replace("do", "").strip()

            try:
                print("hello") 
                print(search_query)
                summary = wikipedia.summary(query, sentences=2)
                print(summary)
                speak(summary)
            except Exception as e:
                speak(f"An error occurred: {e}")

        elif "what do" in query:
            search_query = query.replace("what", "").replace("do", "").strip()

            try:
                print("hello") 
                print(search_query)
                summary = wikipedia.summary(query, sentences=2)
                print(summary)
                speak(summary)
            except Exception as e:
                speak(f"An error occurred: {e}")

        elif "who is" in query:
            search_query = query.replace("who", "").replace("is", "").strip()

            try:
                # print("hello") 
                print(search_query)
                summary = wikipedia.summary(query, sentences=2)
                print(summary)
                speak(summary)
            except Exception as e:
                speak("An error occurred")