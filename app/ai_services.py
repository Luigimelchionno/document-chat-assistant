from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY non trovata. Verifica le variabili d'ambiente.")

client = OpenAI(api_key=OPENAI_API_KEY)

def analyze_text(text):
    prompt = f"""
    Esegui un'analisi del seguente documento:

    {text[:2000]}

    Fornisci:
    1. Un breve riassunto
    2. I temi principali
    3. 5 domande-chiave sul contenuto
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def chat_with_document(messages, document_text):
    # Aggiungi il contenuto del documento al contesto di GPT
    messages.append({"role": "system", "content": f"Il documento è il seguente:\n{document_text[:1000]}..."})

    # Invia la domanda dell'utente
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message.content

