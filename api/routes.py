from fastapi import APIRouter
from models.request import ChatRequest
from models.response import ChatResponse
from services.chatbot import process_chat

router = APIRouter()
#Defines the API endpoints for handling requests and responses.
@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(chat_request: ChatRequest):
    response = process_chat(chat_request.message)
    return ChatResponse(reply=response)