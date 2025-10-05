# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt gunicorn \
    && apt-get update \
    && apt-get install -y sudo docker.io \
    && rm -rf /var/lib/apt/lists/*

# Create Jenkins user and add to docker group
RUN groupadd -g 999 docker || true \
    && useradd -m -u 1000 -G docker jenkins \
    && echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Copy entrypoint
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Expose port
EXPOSE 5000

# Use entrypoint
ENTRYPOINT ["docker-entrypoint.sh"]

# Default CMD
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]