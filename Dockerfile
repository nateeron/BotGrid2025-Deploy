# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed dependencies
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 45441

# Run uvicorn to serve the FastAPI app
CMD ["uvicorn", "FastAPI_BotGrid2025:app", "--host", "0.0.0.0", "--port", "45441"]

