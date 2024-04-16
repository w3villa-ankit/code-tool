# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app


ADD requirements.txt requirements.txt 
RUN python -m pip install -r requirements.txt

# Switch to the non-privileged user to run the application.

# Copy the source code into the container.
COPY . .

# Expose the port that the application listens on.
EXPOSE 4000

# Run the application.
CMD /bin/bash -lc "uvicorn 'main:app' --host=0.0.0.0 --port=4000"
