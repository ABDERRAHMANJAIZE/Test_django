# Use the official Python image from the Docker Hub
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Collect staticfiles files
RUN python manage.py collectstatic --noinput

# Start gunicorn
CMD ["gunicorn", "SFR.wsgi:application", "--bind", "0.0.0.0:8000"]
