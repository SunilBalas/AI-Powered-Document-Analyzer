import streamlit as st

model = "llama-3.1-70b-versatile"
groq_api_key = st.secrets['GROQ_API_KEY']   # Paste your Groq API Key

config = {
    "model": model,
    "groq_api_key": groq_api_key
}