from pydantic import BaseModel
#Defines the structure of the input data using Pydantic
class ChatRequest(BaseModel):
    message: str