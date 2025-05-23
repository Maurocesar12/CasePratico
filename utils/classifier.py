from transformers import pipeline

# Novo modelo mais preciso
classifier = pipeline("text-classification", model="papluca/xlm-roberta-base-language-detection")

def classify_email(text):
    result = classifier(text)[0]['label']
    return "Produtivo" if result == "POSITIVE" else "Improdutivo"
