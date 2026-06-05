FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application (app + scripts, if needed for seeding)
COPY ./app ./app
COPY ./scripts ./scripts

# Expose the FastAPI port
EXPOSE 8000

# Run the API server (environment variables must be provided at runtime)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]