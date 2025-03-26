import pyttsx3
from gtts import gTTS
import os

def speak_text(text, lang="en"):
    """
    Convert text to speech in the specified language.
    Uses gTTS for non-English languages and pyttsx3 for English.
    """
    if lang == "en":
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)  # Set to English voice
        engine.say(text)
        engine.runAndWait()
    else:
        # Use gTTS for Hindi and Marathi
        tts = gTTS(text=text, lang=lang)
        tts.save("response.mp3")
        os.system("start response.mp3")  # Plays audio on Windows

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    language = input("Enter language code (en, hi, mr): ").strip().lower()
    speak_text(text, language)
