#!/bin/bash

# Start Flask backend in the background
python flag.py &

# Start Streamlit frontend (modify the port to use Render's PORT env variable)
streamlit run app_ui.py --server.port=$PORT
