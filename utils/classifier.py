import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env

# Configuração do Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

def classify_email(text: str) -> str:
    try:
        prompt = f"""
        Classifique este e-mail como "Produtivo" ou "Improdutivo":
        
        Regras:
        - Assuntos de trabalho, prazos, tarefas = Produtivo
        - Comunicações informais, spam, pessoal = Improdutivo
        
        E-mail: {text[:2000]}  # Limita o tamanho
        
        Responda APENAS com "Produtivo" ou "Improdutivo".
        """
        
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Erro no Gemini: {e}")
        return "Improdutivo (erro)"