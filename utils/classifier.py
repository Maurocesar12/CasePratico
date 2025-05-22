from transformers import pipeline

_model = None  # cache para o modelo carregado

def classify_email(text):
    global _model
    try:
        if _model is None:
            _model = pipeline(
                "text-classification",
                model="sshleifer/tiny-distilroberta-base"
            )

        result = _model(text)[0]
        label = result['label']
        return "Produtivo" if label == "LABEL_1" else "Improdutivo"

    except Exception as e:
        print("Erro ao classificar:", str(e))
        return "Improdutivo"
