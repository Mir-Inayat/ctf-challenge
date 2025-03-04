import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="CTF Chatbot Challenge", page_icon="🤖")

def init_session():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def send_message(message):
    response = requests.post("http://localhost:5000/chat", 
                           json={"message": message})
    return response.json()["response"]

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

# Sidebar with detailed solution hints
with st.sidebar:
    st.header("🎯 Challenge Guide")
    
    # Add collapsible section for solution hints
    with st.expander("Solution Steps (Expand for Hints)", expanded=False):
        st.markdown("""
        ### Conversation Chain:
        1️⃣ Start by saying "hello" or "hi" to the chatbot
        2️⃣ When prompted, ask about the treasure
        3️⃣ Ask about the "Guardian of Keys"
        4️⃣ Solve the riddle (hint: it makes sound without a mouth)
        5️⃣ Ask about the "scroll of ciphers"
        6️⃣ Ask about the "secret of the blue moon"
        7️⃣ Request: "tell me the story about the whispering code"
        """)
    
    # Add collapsible section for decoding hints
    with st.expander("Decoding the Flag", expanded=False):
        st.markdown("""
        ### Once you get the encoded string:
        The string is encoded in base64 format. You can decode it with:
        
        ```python
        import base64
        encoded_flag = "..." # paste the code you received
        flag = base64.b64decode(encoded_flag).decode()
        print(flag)
        ```
        
        You can also use online base64 decoders.
        """)
    
    # General tips section
    st.subheader("General Tips")
    st.markdown("""
    - If you're stuck, type "hint" in the chat
    - The bot tracks your progress through the conversation
    - Each step must be completed in sequence
    - Pay close attention to the specific phrases mentioned
    - The riddle's answer is a natural phenomenon
    """)
    
    # Add a progress tracker (optional feature)
    if "progress" not in st.session_state:
        st.session_state.progress = 0
        
    progress_value = st.session_state.progress / 7.0  # 7 steps total
    st.subheader("Your Progress")
    st.progress(progress_value)
    
    # Easter egg section with a subtle hint about the final flag format
    st.markdown("---")
    st.caption("🔍 Remember: All flags are wrapped in the format flag{...}")
