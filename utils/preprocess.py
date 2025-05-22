import re
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = re.sub(r"[^a-zA-Z ]", "", text.lower())  # remove pontuação e coloca tudo em minúsculo
    words = text.split()
    clean_words = [lemmatizer.lemmatize(word) for word in words if len(word) > 2]
    return " ".join(clean_words)
