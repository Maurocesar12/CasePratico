from transformers import pipeline

try:
    classifier = pipeline("text-classification", model="sshleifer/tiny-distilroberta-base")
except Exception as e:
    classifier = None
    print("Erro ao carregar modelo IA:", e)

def classify_email(text):
    if classifier:
        try:
            result = classifier(text)[0]['label']
            return "Produtivo" if result == "LABEL_1" else "Improdutivo"
        except:
            pass
    return "Improdutivo"
