# Start with a lightweight Python image
FROM python:alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the app.py and requirements.txt from the current directory on the host to /app in the container
ADD app.py /app/
ADD requirements.txt /app/

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Set the default command to run when the container starts
CMD ["python", "app.py"]
