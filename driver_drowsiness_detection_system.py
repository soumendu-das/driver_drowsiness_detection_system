import streamlit as st
import google.generativeai as genai
import playsound
from PIL import Image
import os

# Define API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAk3XfMjeiivTSZ9MYHNMmHetTV7GR_Ar0"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

# Alarm section
st.title("🚖 Real-time Eye State Detection")

def play_alarm():
    try:
        playsound.playsound("warning_alarm.mp3")
    except Exception as e:
        st.error(f"Error playing alarm sound: {e}")

uploaded_image = st.file_uploader("Upload an image:")

prompt = "You are best in photo analysis, so only detect if eyes are open or not. If eyes are open, say yes, otherwise say no."

if uploaded_image:
    try:
        image = Image.open(uploaded_image)
        
        response = model.generate_content([
            prompt,
            image,
        ])
        
        # Check if response.text is available and valid
        if hasattr(response, 'text') and response.text:
            st.write(response.text)
            if response.text.lower() == "no":
                play_alarm()
        else:
            st.error("No valid response from model.")
    
    except Exception as e:
        st.error(f"Error processing the image: {e}")
