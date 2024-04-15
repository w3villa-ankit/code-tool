# create a fast api app

from fastapi import FastAPI
from pydantic import BaseModel
from dockerCommandLineCodeExecutor import dockerCommandLineCodeExecutor
from jupyterCodeExecuter import jupyterCodeExecuter

app = FastAPI()

class Item(BaseModel):
    message: str

@app.post("/code")
async def run_code(item: Item):
    chat_result = dockerCommandLineCodeExecutor(item) # Use this line to run the docker command line code executor
    # chat_result = jupyterCodeExecuter(item) # Use this line to run the jupyter code executor
    return {"chat_result": chat_result.chat_history[1]['content']}

