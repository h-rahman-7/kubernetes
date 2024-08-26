# Use a specific Python base image for more consistent results
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY app.py requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python", "app.py"]
