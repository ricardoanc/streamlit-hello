import streamlit as st
import requests

# Title and setup
st.set_page_config(page_title="Gemma Chatbot", layout="centered")
st.title("💬 Chat with Gemma 3 (Local via Ollama)")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("You:", key="user_input")

# Send message on enter
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    try:
        # Call Ollama API
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:4b",
                "prompt": user_input
            }
        )
        reply = response.json().get("response", "Hmm… no reply received.")
        st.session_state.chat_history.append({"role": "bot", "content": reply})

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Display conversation
for msg in st.session_state.chat_history:
    emoji = "🧑" if msg["role"] == "user" else "🤖"
    st.markdown(f"**{emoji} {msg['content']}**")
    