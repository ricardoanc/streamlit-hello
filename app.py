import streamlit as st

name = st.text_input("What is your name?")

if name:
    st.write(f"Hi {name}, nice to meet you!")