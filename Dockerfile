# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends libmagic1 \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

ENV PORT=8000
CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn textstore.wsgi:application --bind 0.0.0.0:${PORT} --workers 2 --timeout 90 --access-logfile - --error-logfile -"]
