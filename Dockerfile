FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y supervisor

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copy supervisor configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 5000 8501

CMD ["/usr/bin/supervisord"]
