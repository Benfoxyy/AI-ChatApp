from openai import OpenAI
import streamlit as st

st.title("AI Chat APP with Streamlit 🤖")

client = OpenAI(api_key=st.secrets["openai"]["api_key"])
message = st.chat_input("What is on your mind?")

# Ensure both the API key and the message are provided
if message:
    def stream_openai_response():
        # Using openai.chat.Completion.create for new API
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # Model selection
            messages=[{"role": "user", "content": message}],  # Messages array as expected
            # store=True,
            stream=True  # Enables streaming response
        )

        # Stream the response and yield content in chunks
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content

    # Using st.container() for displaying the stream
    with st.container():
        with st.chat_message("user"):
            st.write(message)
        with st.chat_message("assistant"):
            st.write_stream(stream_openai_response)
