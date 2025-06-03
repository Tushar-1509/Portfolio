import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# ========== Speak Function ==========
def speak(text):
    engine.say(text)
    engine.runAndWait()

# ========== News API Function ==========
def get_news(api_key, topic="technology"):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={"9ddfc70a8da94e1b9a574356c31161ad"}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])

    if not articles:
        speak("Sorry, I couldn't find any news on that topic.")
        return

    speak(f"Here are the top {min(3, len(articles))} news headlines about {topic}:")
    for i, article in enumerate(articles[:3]):
        print(f"{i+1}. {article['title']}")
        speak(article['title'])

# ========== Weather Function ==========
def get_weather_by_city(city):
    api_key = "bea637738234e6d524ad7f1e32daf0d6" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            speak("Sorry, I couldn't find the weather for that city.")
            return

        weather_main = data["weather"][0]["main"]
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        pressure = data["main"]["pressure"]

        print(f"The weather in {city} is {weather_main} with {weather_desc}.")
        speak(f"The weather in {city} is {weather_main} with {weather_desc}.")
        print(f"The temperature is {temp} degrees Celsius and pressure is {pressure} hectopascals.")
        speak(f"The temperature is {temp} degrees Celsius and pressure is {pressure} hectopascals.")

    except Exception as e:
        speak("Sorry, I couldn't get the weather information due to an error.")
        print(e)

# ========== Command Processing ==========
def processcommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif c.startswith("play"):
        parts = c.split(" ", 1)
        if len(parts) > 1:
            song = parts[1]
            link = musiclibrary.music.get(song)
            if link:
                webbrowser.open(link)
            else:
                speak("I couldn't find that song.")
        else:
            speak("Please say the song name.")
    elif "news" in c:
        topic = "technology"
        if "about" in c:
            topic = c.split("about")[-1].strip()
        get_news("YOUR_NEWS_API_KEY", topic)  
    elif "weather" in c:
        if "in" in c:
            city = c.split("in")[-1].strip()
            get_weather_by_city(city)
        else:
            speak("Please say the city name, like 'weather in Delhi'.")

# ========== Main Loop ==========
if __name__ == "__main__":
    speak("Initializing Jarvis...")

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            while True:
                try:
                    print("Listening for wake word...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
                    wake_word = recognizer.recognize_google(audio).lower()

                    if "jarvis" in wake_word:
                        speak("Yes?")
                        print("Jarvis activated. Listening for command...")
                        audio = recognizer.listen(source, timeout=6, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        print("Command received:", command)
                        processcommand(command)

                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results from Google; {e}")
                except Exception as e:
                    print(f"Error: {e}")
    except Exception as mic_error:
        print(f"Microphone not accessible: {mic_error}")
        speak("Sorry, I couldn't access the microphone.")
