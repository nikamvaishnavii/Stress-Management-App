import streamlit as st
import speech_recog as sr_module
import ai_response
import text_to_speech as tts
import youtube_videos
import music_player
import games
from streamlit_lottie import st_lottie
import requests
import pyttsx3
import random
from transformers import pipeline

# Load Generative AI Model (Using Hugging Face's GPT-based model)
story_generator = pipeline("text-generation", model="gpt2")

# Function to Load Lottie Animation
def load_lottie_url(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except requests.exceptions.RequestException:
        pass
    return None

# Fetch Lottie Animations
animations = {
    "welcome": load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_ydo1amjm.json"),
    "music": load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_mgqwhmqc.json"),
    "chat": load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_x62chJ.json")
}

# Streamlit UI Configuration
st.set_page_config(page_title="Stress Management Assistant", page_icon="🌟", layout="wide")

# Custom UI Styling with Dark Mode & Glassmorphism
st.markdown("""
    <style>
    body { background: url('https://source.unsplash.com/1600x900/?nature,relax') no-repeat center fixed; background-size: cover; }
    [data-testid="stSidebar"] { background: rgba(255, 255, 255, 0.2); border-radius: 15px; backdrop-filter: blur(10px); }
    h1 { text-align: center; color: #4A90E2; font-size: 40px; text-shadow: 2px 2px 8px #aaa; }
    .stButton button { width: 100%; padding: 12px; border-radius: 12px; font-size: 18px; background: linear-gradient(135deg, #ff9a9e, #fad0c4); color: black; border: none; transition: 0.3s; box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2); }
    .stButton button:hover { transform: scale(1.08); background: linear-gradient(135deg, #fad0c4, #ff9a9e); }
    .stTextInput input { border-radius: 10px; border: 1px solid #ccc; padding: 10px; }
    </style>
""", unsafe_allow_html=True)

# Title & Welcome Animation
if animations["welcome"]:
    st_lottie(animations["welcome"], height=250, key="welcome")
st.markdown("<h1>🎧 Stress Management AI Assistant 🎧</h1>", unsafe_allow_html=True)

# Function to generate bedtime story
def generate_story(prompt):
    story = story_generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
    return story

# Function for text-to-speech (TTS)
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to generate soothing soundscape text
def generate_soundscape():
    soundscapes = [
        "Imagine gentle raindrops falling on leaves, a soft rhythm to calm your mind.",
        "Waves crash softly onto the shore, a distant seagull calls, the ocean breeze soothes your soul.",
        "A quiet forest at dusk, crickets chirping, a soft wind rustling the leaves above.",
        "A mountain stream flowing over smooth rocks, its gentle babbling a natural lullaby."
    ]
    return random.choice(soundscapes)

# Sidebar Navigation
st.sidebar.title("✨ Features")
option = st.sidebar.radio(
    "💡 Choose an action:", 
    ["🎤 Speak", "🎵 Play Music", "🧘 Watch Meditation Video", "💃 Watch Dance Video", 
     "🎶 Watch Music Video", "🎮 Play a Game", "🤖 Chat with AI", "🌙 Sleep Improvement"]
)

# Feature: Sleep Improvement
if option == "🌙 Sleep Improvement":
    st.markdown("## 🌙 Sleep Improvement with AI")
    if st.button("Generate Soothing Soundscape"):
        soundscape = generate_soundscape()
        st.write(soundscape)
        speak_text(soundscape)
    
    story_prompt = st.text_input("Enter a bedtime story topic:")
    if st.button("Generate AI Bedtime Story") and story_prompt:
        story = generate_story(story_prompt)
        st.write(story)
        speak_text(story)

# Feature: Speak & Get AI Response
elif option == "🎤 Speak":
    st.markdown("## 🎙️ Speak & Get Advice")
    if st.button("🎤 Start Listening"):
        user_text, detected_lang = sr_module.listen_to_speech()
        if user_text:
            st.success(f"**You said:** {user_text} ({detected_lang})")
            ai_reply = ai_response.get_stress_management_tips(user_text)
            st.info(f"🤖 **AI Response:** {ai_reply}")
            tts.speak_text(ai_reply, detected_lang)
        else:
            st.warning("⚠️ Could not recognize speech. Please try again.")

# Other Features Remain Unchanged
elif option == "🎵 Play Music":
    st.markdown("## 🎶 Stress-Relief Music")
    if animations["music"]:
        st_lottie(animations["music"], height=150, key="music")
    if st.button("▶️ Play Music"):
        music_player.play_music()

elif option == "🧘 Watch Meditation Video":
    st.markdown("## 🧘 Relax with a Meditation Video")
    if st.button("📺 Play Meditation Video"):
        video_url = youtube_videos.get_meditation_video()
        if video_url:
            st.video(video_url)
        else:
            st.error("⚠️ Unable to fetch a meditation video. Try again.")

elif option == "🎮 Play a Game":
    st.markdown("## 🎮 Play a Fun Game")
    games.launch_game()

elif option == "🤖 Chat with AI":
    st.markdown("## 💬 Chat with AI for Stress Advice")
    if animations["chat"]:
        st_lottie(animations["chat"], height=150, key="chat")
    user_input = st.text_input("✍️ Type your concern here:")
    if st.button("🤖 Get AI Advice"):
        if user_input.strip():
            ai_reply = ai_response.get_stress_management_tips(user_input)
            st.success(f"🗨️ **AI Says:** {ai_reply}")
            tts.speak_text(ai_reply, "en")
        else:
            st.warning("⚠️ Please enter a valid input.")
