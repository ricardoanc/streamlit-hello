import streamlit as st

name = st.chat_input("What is your name?")

if name == True:
    st.write('Nice to meet you' + name)
else:
    st.write('Invalid')