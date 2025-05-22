import re

def clean_text(text):
    # Remove caracteres especiais e pontuação
    text = re.sub(r"[^a-zA-Z ]", " ", text)
    text = re.sub(r"\s+", " ", text)  # remove espaços duplicados
    words = [word.lower() for word in text.split() if len(word) > 2]
    return " ".join(words)

