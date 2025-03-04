#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Starting Flask backend (flag.py)..."
python flag.py &

echo "Starting Streamlit frontend (app_ui.py)..."
streamlit run app_ui.py &

echo "Deployment complete! Access the application at http://localhost:8501"
