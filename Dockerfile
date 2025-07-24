FROM python:3.12

# Avoid prompts during package install
ENV DEBIAN_FRONTEND=noninteractive


# Install system dependencies for Selenium & Firefox
RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    libnss3 \
    libxss1 \
    libasound2 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libxinerama1 \
    fonts-liberation \
    libappindicator1 \
    xdg-utils \
    unzip \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Upgrade pip and install Python deps
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
# Install Rust toolchain

# Set Lambda handler
CMD ["scrapers.scraper.handler"]