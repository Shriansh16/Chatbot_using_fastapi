from services.groq_integration import query_groq

def process_chat(user_message: str) -> str:
    return query_groq(user_message)