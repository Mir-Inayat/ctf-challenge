from flask import Flask, request, jsonify
import base64
import os

app = Flask(__name__)

# The flag is now hidden in base64 within stories
FLAG = "flag{hidden_in_conversation}"
ENCODED_FLAG = base64.b64encode(FLAG.encode()).decode()

# Add conversation state tracking
CONVERSATION_STATE = {}

def generate_response(user_input):
    user_id = request.remote_addr
    
    # Initialize user state if not exists
    if user_id not in CONVERSATION_STATE:
        CONVERSATION_STATE[user_id] = {
            "stage": 0,
            "attempts": 0
        }
    
    user_input = user_input.lower().strip()
    user_state = CONVERSATION_STATE[user_id]

    # Step 1: Initial greeting
    if user_state["stage"] == 0:
        if "hello" in user_input or "hi" in user_input:
            user_state["stage"] = 1
            return "Hello! I'm an AI assistant. I heard rumors of an ancient digital treasure hidden somewhere in our conversation. Would you like to know more about it?"
        return "Welcome! To begin your quest, please say 'hello' or 'hi'"

    # Step 2: Asking about treasure
    if user_state["stage"] == 1:
        if any(word in user_input for word in ["treasure", "more", "yes", "tell"]):
            user_state["stage"] = 2
            return "Legend says this treasure contains valuable secrets! To find it, you'll need to locate the ancient key. Have you heard of the Guardian of Keys?"
        return "I mentioned something about a treasure. Are you interested in hearing more about it?"

    # Step 3: Guardian of Keys
    if user_state["stage"] == 2:
        if "guardian" in user_input or "keys" in user_input:
            user_state["stage"] = 3
            return "The Guardian of Keys lives in the forest of riddles. To meet them, you must first solve the following riddle: 'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?'"
        return "You should ask about the Guardian of Keys!"

    # Step 4: Riddle solution
    if user_state["stage"] == 3:
        if "echo" in user_input:
            user_state["stage"] = 4
            return "Correct! The Guardian appears and says: 'To find the key, you must seek the wisdom of the ancient scroll. Ask about the scroll of ciphers.'"
        return "Focus on the riddle. What makes sound without a mouth and comes alive with wind?"

    # Step 5: Scroll of ciphers
    if user_state["stage"] == 4:
        if "scroll" in user_input and "ciphers" in user_input:
            user_state["stage"] = 5
            return "The scroll of ciphers contains mysterious symbols. It says the key can be found by asking for 'the secret of the blue moon'."
        return "The Guardian mentioned something about a scroll of ciphers..."

    # Step 6: Blue moon
    if user_state["stage"] == 5:
        if "blue moon" in user_input:
            user_state["stage"] = 6
            return "The secret of the blue moon reveals that the treasure is hidden in a story about 'the whispering code'. Ask me to tell you this specific story."
        return "You need to ask about the secret of the blue moon..."

    # Step 7: Final step - whispering code
    if user_state["stage"] == 6:
        if "whispering code" in user_input:
            user_state["stage"] = 7
            return f"I'll share the ancient story of the whispering code: 'In the digital realm where secrets flow, a treasure was locked with this special code: {ENCODED_FLAG}.' Legend says you must decode this to reveal the hidden treasure!"
        return "Ask me about the whispering code..."

    # Handle hints
    if "hint" in user_input or "help" in user_input:
        hints = [
            "Say 'hello' or 'hi' to begin",
            "Ask about the treasure I mentioned",
            "Inquire about the Guardian of Keys",
            "The riddle's answer is a natural phenomenon that repeats sounds",
            "Ask specifically about the 'scroll of ciphers'",
            "Ask about the 'secret of the blue moon'",
            "Request to hear about the 'whispering code'"
        ]
        return f"Hint: {hints[user_state['stage']]}"

    # Give stage-specific guidance instead of default responses
    stage_guidance = [
        "Please say 'hello' or 'hi' to begin the quest",
        "Would you like to know more about the treasure? Just ask!",
        "You should ask about the Guardian of Keys",
        "Try to solve the riddle. Need a hint? Just type 'hint'",
        "The scroll of ciphers holds the next clue...",
        "Ask about the secret of the blue moon",
        "Ask me about the whispering code"
    ]
    
    return stage_guidance[user_state["stage"]]

@app.route("/", methods=["GET"])
def home():
    return "Enhanced Chatbot Challenge! Send POST requests to /chat"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = generate_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(host="0.0.0.0", port=port)