import streamlit as st 
import google.generativeai as genai

import os
from PIL import Image

#define api key
os.environ["GOOGLE_API_KEY"]="AIzaSyAk3XfMjeiivTSZ9MYHNMmHetTV7GR_Ar0"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model=genai.GenerativeModel("gemini-2.0-flash")
#-------------------------------------------------------------------------------------

#alarm section

    
uploaded_image=st.file_uploader("upload :")

prompt="you are best in photo analysis so only you detect eyes is open or not is eyes are open then say yes if not then say no "
if uploaded_image:
    image=Image.open(uploaded_image)
    response=model.generate_content([
        prompt,
        image,
        ])
    
    if response.text=="no":
        st.write(response.text)
        
    else:
        st.write(response.text)
