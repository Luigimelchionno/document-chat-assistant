# Document Chat Assistant

## Descrizione
Un'applicazione web che permette agli utenti di caricare un documento (PDF), estrarre il testo, analizzarlo tramite GPT-3, e interagire con il documento tramite una chat.
 Le funzionalità principali includono:
- Caricamento di file PDF
- Analisi automatica dei documenti (riassunto, temi principali, domande chiave)
- Chat con GPT per rispondere alle domande sull'analisi
- Salvataggio della cronologia delle conversazioni

## Installazione

1. Clona questo repository:
   ```bash
   git clone https://github.com/Luigimelchionno/document-chat-assistant.git


2.Utilizzo del progetto:
    Installa le dipendenze usando pip install -r requirements.txt.

    Configura la chiave API in un file .env nella radice del progetto con:
        OPENAI_API_KEY=la-tua-api-key
    Avvia l'app con il comando python main.py e visita http://localhost:5000
