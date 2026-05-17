FROM python:3.11-slim

# Install Chromium + dependencies for Selenium
RUN apt update && apt install -y \
    chromium \
    chromium-driver \
    libnss3 \
    libgbm1 \
    libxkbcommon0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxfixes3 \
    libxi6 \
    libxtst6 \
    libcups2 \
    libxss1 \
    libasound2 \
    libatspi2.0-0 \
    fonts-liberation \
    xdg-utils \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for Chrome/Selenium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER=/usr/bin/chromedriver
ENV PATH="/usr/bin:${PATH}"
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
ENV SELENIUM_REMOTE_URL=http://localhost:4444

# Create app directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot code
COPY moy.py .

# Create downloads directory
RUN mkdir -p /app/downloads

# Set permissions
RUN chmod +x moy.py

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD python -c "import telebot, requests, selenium; print('OK')" || exit 1

# Run the bot
CMD ["python", "moy.py"]
