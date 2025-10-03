import streamlit as st
import google.generativeai as genai

# -----------------------------
# Configure Gemini API
# -----------------------------
api_key = "AIzaSyD1ZtxK2RBGDzcKIHZ0QsGbCqaGv3qDi3o"
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="AI Q&A Bot", page_icon="🤖", layout="wide")
st.markdown("<h1 style='text-align: center;'>🤖 AI Q&A Bot </h1>", unsafe_allow_html=True)

# -----------------------------
# Initialize session state
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# -----------------------------
# Containers
# -----------------------------
chat_container = st.container()   # chat messages
input_container = st.container()  # input box

# -----------------------------
# Input box at bottom
# -----------------------------
with input_container:
    st.session_state.user_input = st.text_input("Type your message here...", value=st.session_state.user_input, key="input_box")
    
    if st.button("Send") and st.session_state.user_input:
        question = st.session_state.user_input
        try:
            response = model.generate_content(question)
            answer = response.text
            st.session_state.history.append((question, answer))
            st.session_state.user_input = ""  # clear input
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")

# -----------------------------
# Chat display (scrollable)
# -----------------------------
with chat_container:
    for q, a in st.session_state.history:
        # User message
        st.markdown(f"""
        <div style='display:flex; margin-bottom:10px;'>
            <div style='font-size:24px; margin-right:8px;'>🧑</div>
            <div style='background-color:#DCF8C6; padding:10px; border-radius:12px; max-width:70%;'>{q}</div>
        </div>
        """, unsafe_allow_html=True)

        # AI message
        st.markdown(f"""
        <div style='display:flex; margin-bottom:10px;'>
            <div style='font-size:24px; margin-right:8px;'>🤖</div>
            <div style='background-color:#E6E6FA; padding:10px; border-radius:12px; max-width:70%;'>{a}</div>
        </div>
        """, unsafe_allow_html=True)
