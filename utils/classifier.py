from transformers import pipeline
classifier = pipeline("text-classification", model="distilbert-base-uncased")

def classify_email(text):
    result = classifier(text)[0]['label']
    return "Produtivo" if result == "LABEL_1" else "Improdutivo"