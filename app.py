import streamlit as st
import librosa
import soundfile as sf
import numpy as np

st.title("Noise Suppression App")

# Upload audio file
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

# Function to perform noise suppression
def reduce_noise(audio, sr):
    noise_profile = librosa.effects.split(audio, top_db=30)
    noise_reduced_audio = audio - noise_profile
    return noise_reduced_audio

# If a file is uploaded
if uploaded_file is not None:
    # Load the audio file
    audio, sr = librosa.load(uploaded_file, sr=None)
    st.audio(uploaded_file, format="audio/wav")

    # Display original audio
    st.write("Original Audio")
    st.audio(uploaded_file)

    # Perform noise suppression
    cleaned_audio = reduce_noise(audio, sr)

    # Save the cleaned audio to a file
    output_file = "cleaned_audio.wav"
    sf.write(output_file, cleaned_audio, sr)

    # Display cleaned audio
    st.write("Cleaned Audio")
    st.audio(output_file)

    # Download button
    with open(output_file, "rb") as file:
        st.download_button(label="Download Cleaned Audio", data=file, file_name="cleaned_audio.wav", mime="audio/wav")
