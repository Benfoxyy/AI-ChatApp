import openai
import streamlit as st

st.title("AI Chat APP with Streamlit 🤖")

col1, col2 = st.columns(2)

with col2:
    openai.api_key = st.text_input("Enter your API Key for using AI")
        
with col1:
    message = st.text_input("What is on your mind?")

try:
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
    else:
        st.warning("Please enter your API Key for using AI", icon="⚠️")
except openai.error.AuthenticationError:
    st.error("Invalid API Key!", icon="❌")