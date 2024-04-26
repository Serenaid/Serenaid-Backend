FROM python:3.10-slim

# Install necessary packages
RUN apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade --ignore-installed --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8080

# Command to run the app
CMD ["gunicorn", "--log-level", "debug", "-b", "0.0.0.0:8080", "--timeout", "600", "run:app"]
