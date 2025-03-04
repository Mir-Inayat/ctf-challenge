FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY flag.py .
COPY app_ui.py .
COPY render_start.sh .

# Make the start script executable
RUN chmod +x render_start.sh

# Expose ports for both services
EXPOSE 5000
EXPOSE 8501

# Set environment variables for Render
ENV PORT=10000

# Use the start script as entry point
CMD ["./render_start.sh"]
