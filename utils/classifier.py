from transformers import pipeline
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    classifier = pipeline(
        "text-classification",
        model="philschmid/tiny-distilbert-classification",
        device=-1
    )
    logger.info("Modelo carregado com sucesso!")
except Exception as e:
    logger.error(f"Falha crítica: {e}")
    classifier = None

def classify_email(text: str) -> str:
    if not classifier:
        return "Improdutivo (erro)"
    try:
        result = classifier(text[:512])[0]  # Limita o texto para evitar overload
        return "Produtivo" if result["label"] == "LABEL_1" else "Improdutivo"
    except Exception as e:
        logger.error(f"Erro na classificação: {e}")
        return "Improdutivo (erro)"