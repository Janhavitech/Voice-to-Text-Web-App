import streamlit as st
import speech_recognition as sr

# Streamlit Page Config
st.set_page_config(page_title="Voice-to-Text", page_icon="🎙️", layout="centered")

# Custom Styling
st.markdown("""
    <style>
        .big-font { font-size: 22px !important; }
        .stTextArea textarea { font-size: 18px; }
        .stButton>button { 
            background-color: #FF4B4B; 
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 24px;
        }
        .stButton>button:hover {
            background-color: #C00000;
        }
    </style>
""", unsafe_allow_html=True)

# UI Header
st.markdown("<h1 style='text-align: center;'>🎙️ Voice-to-Text Converter</h1>", unsafe_allow_html=True)
st.write("### Speak into the microphone and get real-time transcription.")

# Speech Recognition Function
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        with st.spinner("Listening... 🎧 Please speak now!"):
            try:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                return "⚠️ Could not understand the audio. Please try again."
            except sr.RequestError:
                return "⚠️ API unavailable. Check your internet connection."
            except Exception as e:
                return f"⚠️ Error: {str(e)}"

# Start Button
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("🎤 Start Recording"):
        result = recognize_speech()
        st.text_area("📝 Transcribed Text:", result, height=150)

# Footer
st.markdown("<br><hr><p style='text-align: center; font-size: 14px;'>✨ Created with ❤️ using Streamlit</p>", unsafe_allow_html=True)


