import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyAwQZ1iIbidgRLROw7eIoRic2CsnpdMRQI")

MODEL_NAME = "gemini-1.5-pro-latest"

def get_stress_management_tips(user_input):
    """Send user input to Gemini AI and return response."""
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"❌ Error: {e}"
