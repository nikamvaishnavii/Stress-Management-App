import speech_recognition as sr

def listen_to_speech():
    """Listen to user's speech and return transcribed text & detected language"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now... (Listening)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="hi-en")
        detected_lang = "hi" if any(word in text for word in ["kaise", "kya", "kyu", "hai"]) else "en"
        print(f"🗣️ You said: {text}")
        return text, detected_lang
    except sr.UnknownValueError:
        print("⚠️ Could not understand audio")
        return "", "en"
    except sr.RequestError:
        print("⚠️ API request failed")
        return "", "en"
