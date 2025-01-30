import openai
import streamlit as st

st.title("AI Chat APP with Streamlit 🤖")

openai.api_key = st.secrets["openai"]["api_key"]
message = st.text_input("What is on your mind?")

if openai.api_key and message:
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