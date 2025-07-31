import streamlit as st

name = st.text_input("What is your name?")

st.write(f'Nice to meet you '+name)