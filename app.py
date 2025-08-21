from flask import Flask, render_template, request
from utils.preprocess import clean_text
from utils.classifier import classify_email
from utils.responder import generate_response
import os, time
from pdfminer.high_level import extract_text  # Adicionei para PDF
from flask import Flask, render_template, request, url_for, send_from_directory

# Configuração de ambiente
os.environ["XFORMERS_IGNORE_MISSING"] = "1"
app = Flask(__name__, static_folder="static", static_url_path="/static")
def asset_url(name: str):
    path = os.path.join(app.static_folder, name)
    v = int(os.path.getmtime(path)) if os.path.exists(path) else int(time.time())
    return url_for("static", filename=name, v=v)

app.jinja_env.globals["asset_url"] = asset_url

# Configurações
UPLOAD_FOLDER = "/tmp/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # Limite de 2MB para uploads

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = ""
        try:
            if "email_text" in request.form and request.form["email_text"].strip():
                content = request.form["email_text"].strip()
                
            elif "email_file" in request.files:
                f = request.files["email_file"]
                
                if f.filename.endswith(".txt"):
                    content = f.read().decode("utf-8")
                    
                elif f.filename.endswith(".pdf"):
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
                    f.save(filepath)
                    content = extract_text(filepath)  # Extrai texto do PDF
                    os.remove(filepath)  # Limpa após uso

            # Processamento e classificação
            processed = clean_text(content)
            categoria = classify_email(processed)
            resposta = generate_response(categoria, content)
            
            return render_template(
                "index.html",
                categoria=categoria,
                resposta=resposta,
                conteudo=content
            )

        except Exception as e:
            print(f"ERRO: {str(e)}")
            return render_template("index.html", error=str(e))

    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)