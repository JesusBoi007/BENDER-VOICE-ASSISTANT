import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import os
import yfinance as yf
import pyjokes
import wikipedia

#listen to our microphone and return the audio as text using google

def transform():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Calibrating for background noise..... please wait")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 0.8
        print("I am listening")
        said = r.listen(source)
        try:
            q = r.recognize_google(said, language = "en")
            print(f"You said: {q}")
            return q
        except sr.UnknownValueError:
            print("Sorry, I did not understand")
            return "I am waiting"
        except sr.RequestError:
            print("Sorry, the service is down")
            return "I am waiting"
        except:
            return "I am waiting"


def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

#Returns the weekday name
def query_day():
    day = datetime.date.today()
    print(day)
    weekday = day.weekday()
    mapping = {0 : "MONDAY", 1 : "TUESDAY", 2 : "WEDNESDAY", 3 : "THURSDAY", 4 : "FRIDAY", 5 : "SATURDAY", 6 : "SUNDAY" }
    print(mapping[weekday])
    try:
        speak(f"Today is {mapping[weekday]}")
    except:
        pass


def query_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")

#INTRO GREETING AT START UP
def welcome():
    speak('''Hello, I am BENDER. 
          I am your personal assistant.
          How may I help you?
    ''')

#the heart of my assistant. Takes queries and return answers
def querying():
    welcome()
    start = True
    while True:
        q = transform().lower()

        if "open youtube" in q:
            speak('Opening Youtube. Just a second')
            webbrowser.open("https://www.youtube.com")
            continue

        elif "open chrome" in q:
            speak("Opening Chrome")
            webbrowser.open('https://www.google.com')
            continue

        elif "what is the time" in q:
            query_time()
            continue

        elif "what day is it" in q:
            query_day()
            continue

        elif "thank you" in q:
            speak("You are welcome. Enjoy the rest of your day")
            break

        elif "from wikipedia" in q:
            speak("Checking wikipedia")
            q = q.replace("wikipedia", "")
            result = wikipedia.summary(q, sentences = 2)
            speak("FOUND ON WIKIPEDIA")
            speak(result)
            continue

        elif "your name" in q:
            welcome()
            continue

        elif "search the internet" in q:
            pywhatkit.search(q)
            speak('This is what I found')
            continue

        elif "play" in q:
            q = q.replace("play", "")
            speak(f"Playing {q}")
            pywhatkit.playonyt(q)
            continue

        elif "joke" in q:
            speak(pyjokes.get_joke)
            continue

        elif "price" in q:
            search = q.split("of")[-1].strip()
            lookup = {"bitcoin": "BTC", "ethereum": "ETH", "solana": "SOL", "sui": "SUI", "xrp": "XRP"}
            
            try:
                crypto = lookup[search]
                crypto = yf.Ticker(crypto)
                currentprice = crypto.info["regularMarketPrice"]
                speak(f"Found it, the price of {search} is {currentprice}")
            except:
                speak("Sorry, I have no data")
            continue

querying()