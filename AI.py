import openai
import streamlit as st

st.title("AI Chat APP with Streamlit 🤖")

openai.api_key = st.secrets["openai"]["api_key"]
message = st.text_input("What is on your mind?")

# Ensure both the API key and the message are provided
if openai.api_key and message:
    def stream_openai_response():
        # Using openai.Completion.create for new API
        response = openai.Completion.create(
            model="gpt-4",
            prompt=message,  # Replaced 'messages' with 'prompt'
            max_tokens=150,  # You can adjust this as needed
            temperature=0.7,  # You can adjust this for creativity
            stream=True  # Enables streaming response
        )

        # Stream the response and yield content in chunks
        for chunk in response:
            if 'choices' in chunk and 'text' in chunk['choices'][0]:
                yield chunk['choices'][0]['text']

    # Using st.container() for displaying the stream
    with st.container():
        st.write_stream(stream_openai_response)
else:
    st.warning("Please enter your API Key and a message to continue.")
