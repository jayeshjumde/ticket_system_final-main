FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Upgrade pip and wheel
RUN pip install --upgrade pip wheel

# Install the required dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables if needed
ENV PYTHONUNBUFFERED=1

# Expose the port the app will run on
EXPOSE 8000

# Command to run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

