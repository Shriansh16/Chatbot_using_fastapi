from pydantic import BaseModel
#Defines the structure of the output data using Pydantic
class ChatResponse(BaseModel):
    reply: str