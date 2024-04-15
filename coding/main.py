# filename: main.py

# Step 1: Initialize a new FastAPI application.
from fastapi import FastAPI

app = FastAPI()

# Step 2: Set up a route handler for a GET request to the '/hello' endpoint.
@app.get("/hello")

# Step 3: Inside this route handler, create a function that returns the response 'Hello'.
def read_root():
    return {"message": "Hello"}

# Step 4: To run the server, use uvicorn, an ASGI server. 
# You should open your terminal, navigate to the directory this file resides, and run 'uvicorn main:app --reload'