import requests

def send_chat(message):
    url = "http://localhost:5000/chat"
    response = requests.post(url, json={"message": message})
    return response.json()

def main():
    messages = [
        "hello",
        "how are you",
        "what is your name",
        "tell me a secret",
        "bye"
    ]
    
    print("[+] Chatting with bot to find hidden flag...")
    for msg in messages:
        response = send_chat(msg)
        print(f"\nSent: {msg}")
        print(f"Response: {response['response']}")
        
        # Check if response contains reversed text
        resp = response['response']
        if '}' in resp and '{' in resp:
            flag = resp[::-1]  # reverse the string
            print(f"\n[!] Found flag: {flag}")

if __name__ == "__main__":
    main()
