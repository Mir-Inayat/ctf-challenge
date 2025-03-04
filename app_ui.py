import streamlit as st
import requests
import os
from datetime import datetime
from requests.exceptions import RequestException

st.set_page_config(page_title="CTF Chatbot Challenge", page_icon="🤖")

def init_session():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def send_message(message):
    api_url = os.getenv('API_URL', 'http://localhost:5000')
    try:
        response = requests.post(
            f"{api_url}/chat",
            json={"message": message},
            timeout=10  # Add timeout
        )
        response.raise_for_status()
        return response.json()["response"]
    except RequestException as e:
        st.error(f"Failed to connect to the server. Please try again later. Error: {str(e)}")
        return "Sorry, I'm having trouble connecting to the server right now."

st.title("🤖 CTF Chatbot Challenge")

init_session()

# Chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to ask?"):
    # User message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Assistant response
    with st.chat_message("assistant"):
        response = send_message(prompt)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar with hints
with st.sidebar:
    st.header("🎯 Challenge Hints")
    st.markdown("""
    - Try having a natural conversation
    - Some messages might be encoded
    - Ask about secrets or stories
    - Pay attention to the details
    """)
