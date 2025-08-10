from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/summarize/")
def summarize(data: TextInput):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama2:latest",
            "prompt": f"Summarize this:\n\n{data.text}",
            "stream": False
        }
    )
    response.raise_for_status()
    result = response.json()
    return {"summary": result.get("response", "No summary returned.")}
