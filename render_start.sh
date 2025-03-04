#!/bin/bash
set -e

# Start Flask backend in the background
python flag.py &

# Wait for backend to start
sleep 5

# Start Streamlit frontend
streamlit run app_ui.py --server.port=$PORT
