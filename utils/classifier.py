from transformers import pipeline

_model = None

def classify_email(text):
    global _model
    try:
        if not _model:
            _model = pipeline("text-classification", model="sshleifer/tiny-distilroberta-base")
        result = _model(text)[0]
        label = result['label']
        return "Produtivo" if label == "LABEL_1" else "Improdutivo"
    except Exception as e:
        print("Erro ao classificar:", str(e))
        return "Improdutivo"
