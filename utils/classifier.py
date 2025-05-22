from transformers import pipeline
classifier = pipeline(
    "text-classification",
    model="sshleifer/tiny-distilroberta-base"
)

def classify_email(text):
    result = classifier(text)[0]['label']
    return "Produtivo" if result == "LABEL_1" else "Improdutivo"