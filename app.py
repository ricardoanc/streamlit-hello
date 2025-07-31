import streamlit as st

name = st.text_input("What is your name?")

if name:
    st.write(f"Hi {name}, nice to meet you!")
    age = st.number_input("What is your age (in years)?")

    if age:
        birth_year = st.text_input(f"Were you born in {2025-age} or {2025-age+1}")

        if birth_year:
            st.write('thanks!')