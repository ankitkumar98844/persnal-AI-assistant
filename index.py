# improved_jarvis.py
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import difflib
import re
import urllib.parse
import time
import requests

r = sr.Recognizer()
engine = pyttsx3.init()

# ------------------ SPEAK FUNCTION ------------------
def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

# ------------------ TEXT NORMALIZATION ------------------
def normalize(s: str) -> str:
    return re.sub(r'[^a-z0-9]', '', s.lower())

normalized_map = {normalize(k): k for k in musicLibrary.music.keys()}

def find_song_key(recognized_text: str):
    norm = normalize(recognized_text)
    if not norm:
        return None

    if norm in normalized_map:
        return normalized_map[norm]

    for nk in sorted(normalized_map.keys(), key=len, reverse=True):
        if nk in norm:
            return normalized_map[nk]

    words = re.findall(r'[a-z0-9]+', recognized_text.lower())
    for w in words:
        for nk in normalized_map:
            if w and w in nk:
                return normalized_map[nk]

    close = difflib.get_close_matches(norm, list(normalized_map.keys()), n=1, cutoff=0.6)
    if close:
        return normalized_map[close[0]]
    return None

# ------------------ PROCESS COMMAND ------------------
def process_command(raw_cmd: str):
    c = raw_cmd.lower()

    # ---- Open websites ----
    if "open google" in c:
        webbrowser.open("https://google.com")
        return
    if "open youtube" in c:
        webbrowser.open("https://youtube.com")
        return
    if "open facebook" in c:
        webbrowser.open("https://facebook.com")
        return
    if "open linkedin" in c or "open linkden" in c:
        webbrowser.open("https://linkedin.com")
        return

    # ---- Play music ----
    if re.search(r'\bplay\b', c):
        parts = re.split(r'\bplay\b', c, maxsplit=1)
        if len(parts) < 2:
            speak("Please say the song name.")
            return
        song_text = re.sub(r'\bsong\b$', '', parts[1].strip()).strip()
        if not song_text:
            speak("Please say the song name.")
            return

        key = find_song_key(song_text)
        if key:
            link = musicLibrary.music[key]
            speak(f"Playing {key}")
            webbrowser.open(link)
        else:
            speak(f"{song_text} library mein nahi mila. YouTube par search karta hoon.")
            q = urllib.parse.quote_plus(song_text)
            webbrowser.open(f"https://www.youtube.com/results?search_query={q}")
        return

    # ---- NEWS FEATURE ----
    if "news" in c:
        try:
            speak("Fetching top headlines...")

            # Try NewsAPI (optional)
            NEWS_API_KEY = "YOUR_NEWS_API_KEY_HERE"  # optional
            url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
            articles = []

            try:
                r = requests.get(url, timeout=5)
                if r.status_code == 200:
                    data = r.json()
                    articles = data.get("articles", [])[:5]
            except Exception:
                pass

            # Fallback to Google News RSS
            if not articles:
                rss_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
                rss = requests.get(rss_url, timeout=5).text
                titles = re.findall(r"<title>(.*?)</title>", rss)
                articles = [{"title": t} for t in titles[1:6]]  # skip Google News

            if articles:
                for i, article in enumerate(articles, start=1):
                    title = article.get("title", "").strip()
                    if title:
                        speak(f"Headline {i}: {title}")
                        time.sleep(1.2)
            else:
                speak("Sorry, no news available at this time.")
        except Exception as e:
            print("News fetch error:", e)
            speak("Network problem while fetching news.")
        return

    # ---- Default ----
    speak("Command samajh nahi aaya.")

# ------------------ MAIN PROGRAM ------------------
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    print("Microphone list:")
    for i, name in enumerate(sr.Microphone.list_microphone_names()):
        print(i, name)
    print("\n(If default mic is wrong, set device_index in sr.Microphone(device_index=...) )")

    try:
        with sr.Microphone() as source:
            print("Calibrating for ambient noise (1 second)...")
            r.adjust_for_ambient_noise(source, duration=1)
            print("Calibration done. energy_threshold =", r.energy_threshold)
    except Exception as e:
        print("Warning: mic calibration failed:", e)

    while True:
        try:
            with sr.Microphone() as source:
                print("\nListening for wake word...")
                r.pause_threshold = 0.5
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            try:
                heard = r.recognize_google(audio)
                print("Heard:", heard)
            except sr.UnknownValueError:
                print("Could not understand audio\nHeard: None")
                continue
            except sr.RequestError as e:
                print("API request error:", e)
                time.sleep(1)
                continue

            if "jarvis" in heard.lower():
                speak("Yes sir")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    r.pause_threshold = 0.6
                    audio_cmd = r.listen(source, timeout=5, phrase_time_limit=6)
                try:
                    command = r.recognize_google(audio_cmd)
                    print("Command:", command)
                    process_command(command)
                except sr.UnknownValueError:
                    print("Could not understand command.")
                    speak("Sorry, I did not catch that. Please repeat.")
                except sr.RequestError as e:
                    print("API request error while recognizing command:", e)
                    speak("Network error, try again.")
        except KeyboardInterrupt:
            print("Exiting...")
            break
        except Exception as e:
            print("Main loop error:", e)
            time.sleep(0.5)
