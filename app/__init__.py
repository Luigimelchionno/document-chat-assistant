from flask import Flask
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), "uploads")

# Importa i router dopo aver creato l'app
from app import router
