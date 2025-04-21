import streamlit as st 
import google.generativeai as genai
import requests
import playsound
import cv2
import time
import os
from PIL import Image

#define api key
os.environ["GOOGLE_API_KEY"]="AIzaSyAk3XfMjeiivTSZ9MYHNMmHetTV7GR_Ar0"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model=genai.GenerativeModel("gemini-2.0-flash")
#-------------------------------------------------------------------------------------

#alarm section
def play_alarm():
    playsound.playsound("warning_alarm.mp3")
    
#convert pictur bgr to rgb because PIL and gemini only understand RGB picture
def analyze_frame(frame):
    img=Image.formarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
    try:
        response=model.generate_content([
            "Is the person's eyes open or closed?",
            img
            ])
        return response.text
    except Exception as e:
      return str(e)
#---------------------------------------------------------------------------------------------

st.title("🚖 Real-time Eye State Detection ")
run=st.checkbox("Start Camera")

if run:
    cap=cv2.VideoCapture(0)
    eye_closed_count=0 
    frame_display=st.empty()
    result_display=st.empty()
    
    while True:
        ret,frame=cap.read()
        if not ret:
            st.error("camera not found.")
            break
        frame_resized=cv2.resize(frame,(320,240))
        frame_display.image(frame_resized,channels="BGR")
        result=analyze_frame(frame_resized)
        result_display.write(f"Gemini says: {result}")
        if "closed" in result.lower():
            eye_closed_count+=1
        else:
            eye_closed_count=0 
            
        if eye_closed_count >=3:
            st.warning("Eyes closed! Wake up!")
            play_alarm()
            eye_closed_count=0 
        time.sleep(1)
    cap.release()
