FROM python:3.12-slim

# Install required build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    curl \
    git \
    libssl-dev \
    libffi-dev \
    python3-dev \
    cargo \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Upgrade pip and install Python deps
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
# Install Rust toolchain
