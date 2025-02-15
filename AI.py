from models import gpt, gemini
import streamlit as st

# Get input from the user

message = st.chat_input("What is in your mind?")

# Display the title and instructions
st.title("Welcome to BenBot")
st.write("Choose an AI model to run")

# Model selection
model = st.selectbox("Select AI model", ["GPT", "Gemini"],
                    index=None,
                    placeholder="Select a model to continue ...",)

# Check if message is provided and model is selected
with st.container(border=True):
    if message:
        with st.chat_message("user"):
            st.write(message)
        if model == "GPT":
            with st.chat_message("assistant"):
                st.write(gpt.gpt_model(message=message))
        elif model == "Gemini":
            with st.chat_message("assistant"):
                st.write(gemini.gemini_model(message=message))
        else:
            with st.chat_message("assistant"):
                st.write("Please select a model to chat chat")
    else:
        st.write("Please enter a message to get a response from the selected model.")
