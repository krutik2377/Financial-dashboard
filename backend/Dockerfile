# Use the official Python image.
FROM python:3.10

# Set the working directory in the container.
WORKDIR /usr/src/app

# Copy the dependencies file to the working directory
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
