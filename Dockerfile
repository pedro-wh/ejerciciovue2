# Use a lightweight Python image
FROM python:3.7.16-slim

# Environment variable to force stdout/stderr to be unbuffered.
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the Django project code
COPY . /app/

# Expose port 8000 and run the development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py seed && python manage.py runserver 0.0.0.0:8000"]