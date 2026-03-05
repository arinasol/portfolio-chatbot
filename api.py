from fastapi import FastAPI
from pydantic import BaseModel
from bot import ChatBot

app = FastAPI()

bot = ChatBot()

class Message(BaseModel):
    message: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/questions")
def get_questions():
    return {"questions": bot.get_questions()}

@app.post("/chat")
def chat(message: Message):
    answer = bot.get_answer(message.message)
    return {"answer": answer}