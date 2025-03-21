import requests
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama3-8b-8192"

def groq_extract_info(text):
    """Envoie le texte à l'API Groq Cloud pour structurer les informations."""
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
     
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "Tu es une IA spécialisée dans l'extraction et la structuration d'informations."},
            {"role": "user", "content": f"Extrait et structure les informations clés du texte suivant :\n{text}"}
        ],
        "temperature": 0
    }
    
    try:
        response = requests.post(GROQ_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"⚠ Erreur API Groq: {e}"
