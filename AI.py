import openai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# OpenAI API Key (Use secrets management instead of hardcoding)
# openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("OpenAI Chat with Streamlit")

message = st.text_input("What is on your mind?")

if message:
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
    