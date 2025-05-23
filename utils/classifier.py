from transformers import pipeline

# Novo modelo mais preciso
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def classify_email(text):
    result = classifier(text)[0]['label']
    return "Produtivo" if result == "POSITIVE" else "Improdutivo"
