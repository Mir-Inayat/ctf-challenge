@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo Starting Flask backend (flag.py)...
start cmd /k python flag.py

echo Starting Streamlit frontend (app_ui.py)...
start cmd /k streamlit run app_ui.py

echo Deployment complete! Access the application at http://localhost:8501
