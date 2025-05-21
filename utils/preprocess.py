import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# 🔁 Baixa os recursos apenas uma vez
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def clean_text(text):
    # Limpa o texto de símbolos e deixa em minúsculas
    text = re.sub(r"[^a-zA-Z ]", "", text).lower()
    tokens = word_tokenize(text)
    clean = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return " ".join(clean)
