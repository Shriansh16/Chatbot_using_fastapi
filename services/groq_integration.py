from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

def query_groq(message: str) -> str:
    try:
        client = Groq(api_key=os.getenv('GROQ_API_KEY'))
        completion = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a helpdesk chatbot who will answer queries related to healthcare, insurance, finance, retail, and travel in a friendly way. If asked about any other topic, respond with: 'I can only assist with queries related to Healthcare, Insurance, Finance, Retail or Travel.'"
                },
                {
                    "role": "user", 
                    "content": message
                }
            ],
            temperature=0.6,
            max_tokens=1024,
            top_p=1
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"