from fastapi import FastAPI
from api.routes import router as api_router
import uvicorn

app = FastAPI(title="Chatbot with GROQ")
app.include_router(api_router)
#Includes the api_router into the main FastAPI application

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)