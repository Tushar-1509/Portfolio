import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif c.startswith("play"):
        song = c.split(" ", 1)[1]  # safer split
        link = musiclibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("I couldn't find that song.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?q=&language=en&apiKey=3c9047d422764bdc997ca1871f71883c")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles",{})
            for article in articles[:5]:  # Limit to 5 articles for brevity
              title = article.get("title", "No title available")
              speak(title)
    

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                wake_word = recognizer.recognize_google(audio).lower()
                
                if "jarvis" in wake_word:
                    speak("Yes?")
                    with sr.Microphone() as source:
                        print("Jarvis activated. Listening for command...")
                        recognizer.adjust_for_ambient_noise(source, duration=0.3)
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        print("Command received:", command)
                        processcommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google; {e}")
        except Exception as e:
            print(f"Error: {e}")
