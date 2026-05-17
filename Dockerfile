FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV CHROME_BIN=/usr/bin/chromium
ENV PATH="/usr/bin:$PATH"

# Install Chromium + minimal dependencies for headless Selenium
RUN apt update && apt install -y --no-install-recommends \
    chromium \
    chromium-driver \
    libnss3 libgbm1 libxkbcommon0 libx11-xcb1 \
    libxcomposite1 libxcursor1 libxdamage1 libxfixes3 \
    libxi6 libxtst6 fonts-liberation xdg-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy bot code (NO token.txt here)
COPY moy.py .

# Create downloads directory
RUN mkdir -p /app/downloads

# Run the bot
CMD ["python", "-u", "moy.py"]
