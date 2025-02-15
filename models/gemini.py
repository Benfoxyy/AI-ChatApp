from google import genai
import streamlit as st

client = genai.Client(api_key=st.secrets["gemini"]["api_key"])

def gemini_model(message):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=message,
    )
    return response.text