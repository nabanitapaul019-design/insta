# Use Python 3.11 slim as base
FROM python:3.11-slim

# Set environment variables EARLY
ENV DEBIAN_FRONTEND=noninteractive
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER=/usr/bin/chromedriver
ENV PATH="/usr/bin:$PATH"
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true

# Install Chromium + ALL required dependencies for headless mode
RUN apt update && apt install -y --no-install-recommends \
    chromium \
    chromium-driver \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    xdg-utils \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Verify Chrome installation
RUN chromium --version && chromedriver --version

# Create app directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy bot code
COPY moy.py .
COPY token.txt . 2>/dev/null || true

# Create downloads directory with proper permissions
RUN mkdir -p /app/downloads && chmod 777 /app/downloads

# Health check to verify environment
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD python -c "from selenium import webdriver; from selenium.webdriver.chrome.options import Options; opts=Options(); opts.add_argument('--headless'); opts.add_argument('--no-sandbox'); opts.binary_location='/usr/bin/chromium'; print('OK')" || exit 1

# Run the bot
CMD ["python", "-u", "moy.py"]
