import streamlit as st
from gtts import gTTS
import tempfile

# Add background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://t3.ftcdn.net/jpg/08/81/99/54/360_F_881995462_faGZuR7VnpWV3SVE1JDv941MOUrpxea0.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color:black;
    }
    </style>
    """,
    unsafe_allow_html=True
)




st.title("Naveed Text to Speech converter")

user_input = st.text_input("Enter text to speak:",placeholder='This tool is created by Naveed Jat')

if st.button("Speak"):
    if user_input:
        tts = gTTS(user_input)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            tts.save(f.name)
            st.audio(f.name, format="audio/mp3")
    else:
        st.warning("Please enter some text.")
