
# Use an official Python runtime as a parent image
FROM python:3.9.10

# Set the working directory in the container
WORKDIR /app

# Create and activate a virtual environment to avoid using the global Python environment
RUN python -m venv /opt/venv

# Set the virtual environment path to be used by subsequent commands
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip inside the virtual environment
RUN pip install --upgrade pip==24.3.1

# Copy the requirements.txt file first to leverage Docker's layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install -i https://pypi.org/simple -r requirements.txt

# Copy the rest of the application code
COPY . .

# Make port 45441 available to the world outside this container
EXPOSE 45441

# Run uvicorn to serve the FastAPI app
CMD ["uvicorn", "FastAPI_BotGrid2025:app", "--host", "0.0.0.0", "--port", "45441"]
