from flask import render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import uuid

from app import app
from app.utils import extract_text_from_pdf
from app.ai_services import analyze_text, chat_with_document

# In-memory chat history
conversations = {}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Verifica che il campo 'file' sia presente nella richiesta
        if 'file' not in request.files:
            return "Nessun file trovato nella richiesta", 400

        file = request.files['file']

        # Se non è stato selezionato un file, restituire un errore
        if file.filename == '':
            return "Nessun file selezionato", 400

        # Verifica che sia un PDF
        if not file.filename.endswith(".pdf"):
            return "Il file non è un PDF", 400

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Estrai il testo dal PDF
        text = extract_text_from_pdf(filepath)
        analysis = analyze_text(text)

        # Creazione di un nuovo id per la conversazione
        doc_id = str(uuid.uuid4())
        conversations[doc_id] = [{"role": "system", "content": text}]

        return render_template("chat.html", doc_id=doc_id, analysis=analysis)

    return render_template("index.html")


@app.route("/chat/<doc_id>", methods=["POST"])
def chat(doc_id):
    user_msg = request.form.get("message")
    if not user_msg:
        return jsonify({"error": "Messaggio non ricevuto"}), 400

    # Recupera la cronologia
    messages = conversations.get(doc_id)
    if not messages:
        return jsonify({"error": "Documento non trovato"}), 404

    document_text = messages[0]["content"]  # testo del documento PDF

    # Aggiunge il messaggio dell'utente
    messages.append({"role": "user", "content": user_msg})

    # Ottiene la risposta dell'assistente (puoi usare OpenAI o altra AI)
    response = chat_with_document(document_text, messages)

    # Aggiunge la risposta dell'assistente alla cronologia
    messages.append({"role": "assistant", "content": response})

    return jsonify({"reply": response})

