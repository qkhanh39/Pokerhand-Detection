FROM python:3.9-slim

WORKDIR /app

# Copy the requirements.txt and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install system dependencies for rendering and GUI support
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy your source code into the container
COPY ./src /app/src

# Expose the port for Streamlit
EXPOSE 8501

# Set the command to run the app
CMD [ "streamlit", "run", "src/detect.py", "--server.port", "8501"]
