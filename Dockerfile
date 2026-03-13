# Use lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements (we only need Flask)
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY app.py ./app.py
COPY public ./public

# Expose port
EXPOSE 5000

# Set default command
CMD ["python", "app.py"]
