from openai import OpenAI
import streamlit as st

st.title("Welcome To BenBot 🤖")

client = OpenAI(api_key=st.secrets["openai"]["api_key"])

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

message = st.chat_input("What is on your mind?")

if message:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": message})
    with st.chat_message("user"):
        st.markdown(message)

    def stream_openai_response():
        # Create chat completion with full history and selected model
        completion = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=True
        )

        full_response = ""
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                delta_content = chunk.choices[0].delta.content
                full_response += delta_content
                yield delta_content

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

    with st.chat_message("assistant"):
        st.write_stream(stream_openai_response)

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
