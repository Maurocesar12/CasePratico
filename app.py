from flask import Flask, render_template, request
from utils.preprocess import clean_text
from utils.classifier import classify_email
from utils.responder import generate_response
import os
import fitz  # PyMuPDF

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = ""
        if "email_text" in request.form and request.form["email_text"].strip():
            content = request.form["email_text"]
        elif "email_file" in request.files:
            f = request.files["email_file"]
            if f.filename.endswith(".txt"):
                content = f.read().decode("utf-8")
            elif f.filename.endswith(".pdf"):
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
                f.save(filepath)
                with fitz.open(filepath) as doc:
                    for page in doc:
                        content += page.get_text()
        
        processed = clean_text(content)
        categoria = classify_email(processed)
        resposta = generate_response(categoria)

        return render_template("index.html", categoria=categoria, resposta=resposta, conteudo=content)

    return render_template("index.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000, debug=False)
