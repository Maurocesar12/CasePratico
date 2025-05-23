from transformers import pipeline
import os
import logging

# Configura logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cache do modelo (Render não mantém cache entre deploys, mas evita retentativas)
MODEL_CACHE_DIR = "./model_cache"
os.makedirs(MODEL_CACHE_DIR, exist_ok=True)

try:
    classifier = pipeline(
        "text-classification",
        model="philschmid/tiny-distilbert-classification",  # Modelo leve (<10MB)
        cache_dir=MODEL_CACHE_DIR
    )
    logger.info("✅ Modelo carregado!")
except Exception as e:
    classifier = None
    logger.error(f"❌ Falha ao carregar modelo: {e}")

def classify_email(text: str) -> str:
    """Classifica texto como 'Produtivo' ou 'Improdutivo'."""
    if not classifier:
        return "Improdutivo (fallback)"
    
    try:
        result = classifier(text, truncation=True)[0]  # Evita textos longos
        return "Produtivo" if result["label"] == "LABEL_1" else "Improdutivo"
    except Exception as e:
        logger.error(f"Erro na classificação: {e}")
        return "Improdutivo (erro)"