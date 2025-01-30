import openai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# OpenAI API Key (Use secrets management instead of hardcoding)
# openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("OpenAI Chat with Streamlit")

col1, col2 = st.columns(2)

with col2:
    API_Key = st.text_input("Enter your API Key for using AI")
    openai.api_key = API_Key

with col1:
    message = st.text_input("What is on your mind?")

if API_Key and message:
    def stream_openai_response():
        response = openai.ChatCompletion.create(
            stream=True,
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message}],
        )
        for chunk in response:
            if chunk.choices and chunk.choices[0].delta.get("content"):
                yield chunk.choices[0].delta["content"]

    with st.container(border=True):
      st.write_stream(stream_openai_response)
else:
    st.title("Please enter your API Key and message to get a response.")