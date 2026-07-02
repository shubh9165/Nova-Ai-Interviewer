import streamlit as st
from streamlit_mic_recorder import mic_recorder



class Recoder():
    def recorder(self):

        audio = mic_recorder(
            start_prompt="🎤 Start Recording",
            stop_prompt="⏹ Stop Recording",
            just_once=True
        )

        if audio:
            
            with open("answer.wav", "wb") as f:
                f.write(audio["bytes"])

            
            ##st.audio("answer.wav")
        return audio