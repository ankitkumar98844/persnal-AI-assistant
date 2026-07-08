# 🎙️ Jarvis AI Voice Assistant

A Python-based Voice Assistant inspired by J.A.R.V.I.S. from Iron Man. This assistant can recognize voice commands, open websites, play songs from a custom music library, and even fetch the latest news headlines using voice interaction.

---

## ✨ Features

✅ Wake Word Detection ("Jarvis")

✅ Voice Command Recognition

✅ Open Popular Websites
- Google
- YouTube
- Facebook
- LinkedIn

✅ Smart Music Playback
- Play songs from a custom music library
- Fuzzy matching for better song recognition
- Automatic YouTube search if song is not found

✅ Latest News Headlines
- NewsAPI support
- Google News RSS fallback

✅ Text-to-Speech Responses

✅ Error Handling & Microphone Calibration

---

## 📂 Project Structure

```text
Jarvis/
│
├── improved_jarvis.py
├── musicLibrary.py
├── requirements.txt
├── README.md
└── assets/
```

---

## 🛠️ Technologies Used

- Python
- SpeechRecognition
- PyAudio
- pyttsx3
- Requests
- Regex (re)
- Difflib
- Webbrowser Module

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/Jarvis-AI-Voice-Assistant.git
```

### 2. Navigate to Project Folder

```bash
cd Jarvis-AI-Voice-Assistant
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Required Packages

The following packages are required:

```text
SpeechRecognition
pyttsx3
requests
pyaudio
```

You can install them manually:

```bash
pip install SpeechRecognition pyttsx3 requests pyaudio
```

---

## 🎤 PyAudio Installation Guide

### Windows

```bash
pip install pyaudio
```

If installation fails:

```bash
pip install pipwin
pipwin install pyaudio
```

### Linux

```bash
sudo apt-get install portaudio19-dev
pip install pyaudio
```

### macOS

```bash
brew install portaudio
pip install pyaudio
```

---

## 🎵 Music Library Setup

Create a file named:

```python
musicLibrary.py
```

Example:

```python
music = {
    "believer": "https://youtu.be/7wtfhZwyrcc",
    "shape of you": "https://youtu.be/JGwWNGJdvx8",
    "kesariya": "https://youtu.be/BddP6PYo2gs"
}
```

You can add as many songs as you want.

---

## 🚀 Running the Project

Start Jarvis:

```bash
python improved_jarvis.py
```

---

## 🗣️ How to Use

Say:

```text
Jarvis
```

After Jarvis responds:

```text
Yes Sir
```

Give commands such as:

```text
Open Google
```

```text
Open YouTube
```

```text
Play Believer
```

```text
Play Kesariya
```

```text
Tell me the news
```

---

## 📰 News Feature

Jarvis supports:

### Option 1: NewsAPI

Replace:

```python
NEWS_API_KEY = "YOUR_NEWS_API_KEY_HERE"
```

with your own API key.

Get a free API key from:

```text
https://newsapi.org
```

### Option 2: Google News RSS

If no API key is provided, Jarvis automatically fetches headlines through Google News RSS.

---

## 🎯 Example Workflow

```text
User: Jarvis

Jarvis: Yes Sir

User: Open Google

Jarvis opens Google in browser.
```

```text
User: Jarvis

Jarvis: Yes Sir

User: Play Believer

Jarvis plays the song.
```

---

## 🔮 Future Improvements

- Weather Updates
- ChatGPT Integration
- WhatsApp Messaging
- Email Assistant
- AI Conversation Mode
- System Control Commands
- Face Recognition Login
- GUI Dashboard
- Spotify Integration

---

## 🐞 Common Issues

### Microphone Not Detected

Check available microphones:

```python
print(sr.Microphone.list_microphone_names())
```

Then set:

```python
sr.Microphone(device_index=0)
```

with the correct device index.

---

### Speech Recognition Not Working

Check:
- Internet Connection
- Microphone Permissions
- PyAudio Installation

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 👨‍💻 Author

**ANKIT KUMAR**

Python Developer | AI Enthusiast

GitHub:
https://github.com/ankitkumar98844

LinkedIn:
[https://linkedin.com/in/your-profile](https://www.linkedin.com/in/ankit-kumar-71b492255)

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

📢 Share it with others

---

## 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute it for educational purposes.

---

# Thank You ❤️

"Sometimes you gotta run before you can walk."
— Tony Stark
