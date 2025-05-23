from flask import Flask, render_template, request, jsonify
from utils.preprocess import clean_text
from utils.classifier import classify_email
from utils.responder import generate_response
import os
import fitz  # PyMuPDF (cuidado: pesado para o Render Free)

app = Flask(__name__)

# Configurações (Render não mantém arquivos persistentes)
UPLOAD_FOLDER = "/tmp/uploads"  # Usa /tmp/ (diretório temporário)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # Limita uploads a 1MB

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = ""
        try:
            # Processa texto ou arquivo
            if "email_text" in request.form:
                content = request.form["email_text"].strip()
            elif "email_file" in request.files:
                f = request.files["email_file"]
                if f.filename.endswith(".txt"):
                    content = f.read().decode("utf-8")
                elif f.filename.endswith(".pdf"):
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
                    f.save(filepath)
                    with fitz.open(filepath) as doc:
                        content = " ".join(page.get_text() for page in doc)
                    os.remove(filepath)  # Limpa após uso (importante no Render)

            # Classificação e resposta
            processed = clean_text(content)
            categoria = classify_email(processed)
            resposta = generate_response(categoria)
            return render_template("index.html", categoria=categoria, resposta=resposta, conteudo=content)

        except Exception as e:
            return render_template("index.html", error=f"Erro: {str(e)}")

    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render usa porta via env
    app.run(host="0.0.0.0", port=port)