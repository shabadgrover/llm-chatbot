from fastapi import FastAPI

from app.services.chat_service import ChatService
from app.models.chat_models import ChatRequest, ChatResponse


app = FastAPI()

chat_service = ChatService()


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    response = chat_service.chat(request.message)

    return ChatResponse(
        response=response
    )