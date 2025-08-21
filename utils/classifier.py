# utils/classifier.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

def classify_email(text: str) -> str:
    try:
        prompt = f"""
            Classifique este e-mail como "Produtivo" ou "Improdutivo".
            Responda APENAS com uma única palavra: "Produtivo" ou "Improdutivo".
            Preste atenção na classificação.
            Categorias de Classificação para emails:

            - Produtivo: Emails que requerem uma ação ou resposta específica (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema).
            - Improdutivo: Emails que não necessitam de uma ação imediata (ex.: mensagens de felicitações, agradecimentos).
            E-mail:{text[:2000]}
            """
        resp = model.generate_content(prompt)
        raw = (getattr(resp, "text", "") or "").strip()

        # força as duas opções
        low = raw.lower()
        if "produtivo" in low and "improdutivo" not in low:
            return "Produtivo"
        if "improdutivo" in low:
            return "Improdutivo"

        # fallback simples
        return "Produtivo" if "prazo" in low or "erro" in low or "suporte" in low else "Improdutivo"
    except Exception as e:
        print(f"Erro no Gemini: {e}")
        return "Improdutivo"
