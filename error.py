import streamlit as st
from pydub import AudioSegment

st.title("Upload and Process Audio")

uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    try:
        # Attempt to read the audio file
        audio = AudioSegment.from_file(uploaded_file)
        st.success("File uploaded successfully!")
        # Add your audio processing logic here
    except ValueError as ve:
        st.error(f"ValueError: {ve}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
