from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

chatbot = pipeline("text-generation", model="gpt2")

@app.post("/chat")
def chat(request: ChatRequest):
    response = chatbot(request.message, max_length=50)
    return {"reply": response[0]["generated_text"]}
