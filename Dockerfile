# Base Image
FROM python:3.12-slim

# Set Working Directory
WORKDIR /app

# Copy Requirements First
COPY requirements.txt .

# Install Dependencies
RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# Copy Entire Project
COPY . .

# Create Required Directories
RUN mkdir -p \
    uploads \
    outputs \
    logs \
    reports \
    models/department \
    models/sentiment \
    models/urgency

# Expose FastAPI Port
EXPOSE 8000

# Start Application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]