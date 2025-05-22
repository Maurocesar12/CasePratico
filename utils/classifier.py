from transformers import pipeline

# Tenta carregar o modelo leve
try:
    classifier = pipeline(
        "text-classification",
        model="sshleifer/tiny-distilroberta-base"
    )
except Exception as e:
    print("Erro ao carregar o modelo:", str(e))
    classifier = None

def classify_email(text):
    if not classifier:
        return "Improdutivo"
    result = classifier(text)[0]
    label = result['label']
    return "Produtivo" if label == "LABEL_1" else "Improdutivo"
