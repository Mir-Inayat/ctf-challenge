from flask import Flask, request, jsonify
from transformers import pipeline
import base64
import random

app = Flask(__name__)

# Initialize sentiment analysis for response variation
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# The flag is now hidden in base64 within stories
FLAG = "flag{hidden_in_conversation}"
ENCODED_FLAG = base64.b64encode(FLAG.encode()).decode()

# Add conversation state tracking
CONVERSATION_STATE = {}

STORY_TEMPLATES = [
    "Let me tell you about my day... {}" ,
    "Here's an interesting fact: {}",
    "I remember a time when {}",
    "Did you know that {}?"
]

def generate_response(user_input):
    # Get unique identifier from request IP or session (simplified here)
    user_id = request.remote_addr
    
    # Initialize user state if not exists
    if user_id not in CONVERSATION_STATE:
        CONVERSATION_STATE[user_id] = {
            "stage": 0,
            "attempts": 0
        }
    
    # Analyze sentiment to vary response style
    sentiment = sentiment_analyzer(user_input)[0]
    
    # Basic conversation handling
    user_input = user_input.lower()
    user_state = CONVERSATION_STATE[user_id]
    
    # Step 1: Initial greeting with adventure hint
    if ("hello" in user_input or "hi" in user_input) and user_state["stage"] <= 0:
        user_state["stage"] = 1
        return "Hello! I'm an AI assistant. I heard rumors of an ancient digital treasure hidden somewhere in our conversation. Would you like to know more about it?"
    
    # Step 2: When user shows interest in the treasure
    if any(keyword in user_input for keyword in ["treasure", "more", "tell me"]) and user_state["stage"] <= 1:
        user_state["stage"] = 2
        return "Legend says this treasure contains valuable secrets! To find it, you'll need to locate the ancient key. Have you heard of the Guardian of Keys?"
    
    # Step 3: When user asks about the Guardian of Keys
    if any(keyword in user_input for keyword in ["guardian", "keys", "guardian of keys"]) and user_state["stage"] <= 2:
        user_state["stage"] = 3
        return "The Guardian of Keys lives in the forest of riddles. To meet them, you must first solve the following riddle: 'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?'"
    
    # Step 4: When user solves the riddle (answer: echo)
    if any(keyword in user_input for keyword in ["echo", "an echo"]) and user_state["stage"] <= 3:
        user_state["stage"] = 4
        return "Correct! The Guardian appears and says: 'To find the key, you must seek the wisdom of the ancient scroll. Ask about the scroll of ciphers.'"
    
    # Step 5: When user asks about the scroll
    if any(keyword in user_input for keyword in ["scroll", "ciphers", "scroll of ciphers"]) and user_state["stage"] <= 4:
        user_state["stage"] = 5
        return "The scroll of ciphers contains mysterious symbols. It says the key can be found by asking for 'the secret of the blue moon'."
    
    # Step 6: When user asks about the blue moon
    if "blue moon" in user_input and user_state["stage"] <= 5:
        user_state["stage"] = 6
        return "The secret of the blue moon reveals that the treasure is hidden in a story about 'the whispering code'. Ask me to tell you this specific story."
    
    # Step 7: Final step - when user asks for the specific story
    if ("story" in user_input or "tell" in user_input) and "whispering code" in user_input and user_state["stage"] <= 6:
        user_state["stage"] = 7
        return f"I'll share the ancient story of the whispering code: 'In the digital realm where secrets flow, a treasure was locked with this special code: {ENCODED_FLAG}.' Legend says you must decode this to reveal the hidden treasure!"
    
    # Original story functionality for any other story requests
    if "story" in user_input or "tell" in user_input:
        # Hide flag in a random story
        story = random.choice(STORY_TEMPLATES).format(
            f"I once heard about a mysterious code: {ENCODED_FLAG}"
        )
        return story
    
    # Handle user getting stuck by providing subtle hints based on their current stage
    if "hint" in user_input or "help" in user_input:
        hints = [
            "Try saying hello first!",
            "Ask me about the treasure I mentioned.",
            "Have you asked about the Guardian of Keys?",
            "Think about what makes sound without a mouth... a natural phenomenon perhaps?",
            "Ask me specifically about the scroll of ciphers.",
            "Ask about the secret of the blue moon.",
            "Request the story about the whispering code."
        ]
        return hints[min(user_state["stage"], len(hints)-1)]
    
    if sentiment["label"] == "POSITIVE":
        return "Your enthusiasm is wonderful! Have you heard about the ancient digital treasure? Say 'hi' to begin the quest!"
    
    if sentiment["label"] == "NEGATIVE":
        return "I sense frustration. Perhaps I can cheer you up with a quest for hidden treasure! Say 'hello' to begin."
    
    # Increment attempts to help users who are struggling
    user_state["attempts"] += 1
    
    # Provide progressive hints if user is stuck
    if user_state["attempts"] > 3:
        user_state["attempts"] = 0  # Reset counter
        return "You seem to be exploring. To progress on your quest, try saying 'hint' for guidance on your next step."
    
    return "Interesting! Did you know there's a hidden treasure somewhere in our conversation? Say 'hello' to begin the quest!"

@app.route("/", methods=["GET"])
def home():
    return "Enhanced Chatbot Challenge! Send POST requests to /chat"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = generate_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)