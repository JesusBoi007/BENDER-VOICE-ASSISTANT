# 🤖 BENDER – Voice Assistant in Python

BENDER is a simple personal voice assistant built using Python. It can understand spoken commands, perform web searches, tell you the time or date, fetch cryptocurrency prices, and even tell jokes!

---

## 🛠 Features

* 🎧 Voice recognition using Google Speech Recognition API
* 🔊 Speech output using `pyttsx3`
* 🌐 Opens websites like YouTube or Google
* 🕒 Tells the current time and day
* 🧠 Fetches Wikipedia summaries
* 🤣 Tells jokes with `pyjokes`
* 💰 Gets real-time cryptocurrency prices using `yfinance`
* 🎮 Plays YouTube videos using `pywhatkit`

---

## 📆 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, here's what you need manually:

```bash
pip install pyttsx3 SpeechRecognition pywhatkit yfinance pyjokes wikipedia pyaudio
```

> 🔄 Note: On some systems, installing `pyaudio` might require extra steps. If `pip install pyaudio` fails, try:
>
> * `pip install pipwin`
> * `pipwin install pyaudio`

---

## 🚀 How to Run

Make sure your microphone is working.

Then run:

```bash
python voice_assistant.py
```

---

## 📋 Sample Commands You Can Try

* "Open YouTube"
* "What is the time?"
* "What day is it?"
* "Tell me a joke"
* "Search the internet for Python tutorials"
* "Play lo-fi music"
* "What is the price of Bitcoin?"
* "Tell me about Python from Wikipedia"

---

## 🔐 Notes

* This app uses Google’s speech recognition engine, which requires internet access.
* Cryptocurrency data is fetched using Yahoo Finance.

---

## 👨‍💼 Author

Made by **Adeniyi Oluwaseun**
Feel free to contribute, fork, or raise an issue!

---

## 📃 License

This project is open-source and free to use under the MIT License.
