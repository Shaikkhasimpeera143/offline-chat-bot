import streamlit as st
import requests

st.set_page_config(page_title="Offline Chatbot", page_icon="🤖")
st.title("🤖 Offline Chatbot using LLaMA 3")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="user_input")

if user_input:
    st.session_state.chat_history.append(("You", user_input))

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",
        "prompt": user_input,
        "stream": False
    })

    reply = response.json()["response"]
    st.session_state.chat_history.append(("Bot", reply))

st.markdown("---")

for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
