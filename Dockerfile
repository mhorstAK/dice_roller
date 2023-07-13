# Use the official Python 3 base image
FROM python:3

WORKDIR /app

# Set PYTHONPATH to include /app
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

ENV PYTHONUNBUFFERED=1

# Your container needs to listen to Streamlit’s (default) port 8501
EXPOSE 8501

# Your container needs to listen to Streamlit’s (default) port 8501 and check that it's healthy
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the Streamlit app when the container starts
ENTRYPOINT ["streamlit", "run", "apps/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]