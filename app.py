import streamlit as st
import random

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("ChatBot with Streamlit 💬")

user_input = st.text_input("You:", "")

if user_input:
    # Dummy response logic
    responses = ["Interesting!", "Tell me more!", "Why do you think that?"]
    bot_response = random.choice(responses)

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))

# Display chat
for speaker, message in st.session_state.chat_history:
    st.write(f"**{speaker}:** {message}")