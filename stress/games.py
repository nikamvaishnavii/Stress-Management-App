import streamlit as st
import random
import time

def simple_math_game():
    """A basic math addition game with proper input validation."""
    st.write("### Simple Math Game 🧮")

    if "math_question" not in st.session_state:
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        st.session_state.math_question = (num1, num2, num1 + num2)

    num1, num2, correct_answer = st.session_state.math_question

    user_answer = st.text_input(f"What is {num1} + {num2}?", "")

    if st.button("Submit Answer"):
        try:
            user_answer = int(user_answer)
            if user_answer == correct_answer:
                st.success("🎉 Correct! Well done.")
                del st.session_state.math_question  # Reset question after correct answer
            else:
                st.error(f"❌ Incorrect. The correct answer was {correct_answer}. Try again!")
        except ValueError:
            st.error("⚠️ Please enter a valid number!")

def breathing_exercise():
    """A guided breathing relaxation exercise."""
    st.write("### Relaxing Breathing Exercise 🌬️")
    st.write("Follow the breathing instructions below:")

    for _ in range(3):
        with st.spinner("Inhale deeply... 🫁"):
            time.sleep(4)
        with st.spinner("Hold your breath... ⏳"):
            time.sleep(4)
        with st.spinner("Exhale slowly... 💨"):
            time.sleep(6)
    
    st.success("You should feel more relaxed now! 😊")

def rock_paper_scissors():
    """Classic Rock, Paper, Scissors game."""
    st.write("### Rock, Paper, Scissors ✊✋✌️")
    
    choices = ["Rock", "Paper", "Scissors"]
    user_choice = st.selectbox("Choose your move:", choices)
    ai_choice = random.choice(choices)
    
    if st.button("Play"):
        st.write(f"🤖 AI chose: {ai_choice}")
        
        if user_choice == ai_choice:
            st.warning("🤝 It's a tie!")
        elif (user_choice == "Rock" and ai_choice == "Scissors") or \
             (user_choice == "Paper" and ai_choice == "Rock") or \
             (user_choice == "Scissors" and ai_choice == "Paper"):
            st.success("🎉 You win!")
        else:
            st.error("😢 You lose! Try again.")

def memory_test():
    """A game where users remember a sequence of numbers."""
    st.write("### Memory Test 🧠")

    if "memory_sequence" not in st.session_state:
        st.session_state.memory_sequence = [random.randint(0, 9) for _ in range(5)]
        st.session_state.show_sequence = False  # ✅ Fix session state handling

    if st.button("Show Sequence"):
        st.session_state.show_sequence = True  

    if st.session_state.get("show_sequence", False):
        st.write(f"🔢 Memorize this sequence: **{' '.join(map(str, st.session_state.memory_sequence))}**")
        time.sleep(3)
        st.session_state.show_sequence = False  
        st.rerun()  # ✅ Fix rerun issue

    user_input = st.text_input("Enter the sequence after memorizing:")

    if st.button("Submit Sequence"):
        if user_input == " ".join(map(str, st.session_state.memory_sequence)):
            st.success("🎉 Correct! Great memory!")
            del st.session_state.memory_sequence  
        else:
            st.error("❌ Incorrect! Try again.")

def word_scramble():
    """A simple word scramble game where users guess the correct word."""
    st.write("### Word Scramble Game 🔠")

    words = ["streamlit", "relaxation", "meditation", "happiness", "serenity", "mindfulness", "tranquility"]
    
    if "original_word" not in st.session_state:
        st.session_state.original_word = random.choice(words)
        shuffled_word = list(st.session_state.original_word)
        random.shuffle(shuffled_word)
        st.session_state.scrambled_word = "".join(shuffled_word)

    st.write(f"🔀 Scrambled Word: **{st.session_state.scrambled_word}**")

    user_guess = st.text_input("Guess the correct word:")

    if st.button("Submit Answer"):
        if user_guess.strip().lower() == st.session_state.original_word:
            st.success("🎉 Correct! Well done.")
            del st.session_state.original_word  
            del st.session_state.scrambled_word
            st.rerun()  # ✅ Fix rerun issue
        else:
            st.error("❌ Incorrect! Try again.")

def launch_game():
    """Main function to let the user select and play a game."""
    st.write("## 🎮 Stress Relief Games")
    game_choice = st.selectbox("Choose a game to play:", [
        "Select a Game",
        "Simple Math Game",
        "Breathing Exercise",
        "Rock, Paper, Scissors",
        "Memory Test",
        "Word Scramble"
    ])

    if game_choice == "Simple Math Game":
        simple_math_game()
    elif game_choice == "Breathing Exercise":
        breathing_exercise()
    elif game_choice == "Rock, Paper, Scissors":
        rock_paper_scissors()
    elif game_choice == "Memory Test":
        memory_test()
    elif game_choice == "Word Scramble":
        word_scramble()

# Run the game launcher
if __name__ == "__main__":
    launch_game()
