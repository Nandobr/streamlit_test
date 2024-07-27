import streamlit as st

st.write("Hello World !")
movie = st.text_input('Favourite movie?')
st.write(f"My favourite movie is: {movie}")