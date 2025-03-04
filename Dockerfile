FROM python:3.9-slim

WORKDIR /app

# Copy only necessary files
COPY requirements.txt .
COPY flag.py .
COPY app_ui.py .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose port (will use PORT from environment variable)
EXPOSE 8501

# Start both services using streamlit
CMD streamlit run app_ui.py --server.port $PORT
