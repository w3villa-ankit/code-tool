from fastapi import FastAPI    # Import necessary modules

app = FastAPI()    # Create an instance of FastAPI

@app.get("/hello")  # Define endpoint
def read_root():
    return {"message": "Hello"}