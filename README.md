# CTF Chatbot Challenge

A conversational CTF (Capture The Flag) challenge where participants navigate through a series of clues in conversation with an AI chatbot to discover a hidden flag.

## Setup and Deployment

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation & Deployment

#### Automatic Deployment (Recommended)

**Windows:**
1. Open command prompt
2. Navigate to the project directory:
   ```
   cd C:\Users\inayat\Desktop\cccctf
   ```
3. Run the deployment script:
   ```
   deploy.bat
   ```

**Linux/Mac:**
1. Open terminal
2. Navigate to the project directory:
   ```
   cd /path/to/cccctf
   ```
3. Make the script executable:
   ```
   chmod +x deploy.sh
   ```
4. Run the deployment script:
   ```
   ./deploy.sh
   ```

#### Manual Deployment

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Start the Flask backend:
   ```
   python flag.py
   ```

3. Open a new terminal/command prompt and start the Streamlit frontend:
   ```
   streamlit run app_ui.py
   ```

### Accessing the Application

Once both applications are running:

1. The Flask backend runs on: http://localhost:5000
2. The Streamlit frontend runs on: http://localhost:8501

Open your web browser and navigate to http://localhost:8501 to interact with the chatbot.

## Challenge Information

Players must navigate through a conversation chain with the chatbot to discover a hidden flag. The sidebar contains expandable hints to guide participants.

## Troubleshooting

- If you encounter "Address already in use" errors, ensure no other application is using ports 5000 or 8501.
- If the frontend can't connect to the backend, verify that both applications are running.

## Customization

You can modify the flag by editing the `FLAG` variable in `flag.py`.
