import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")
SIGN_OFF = ("\n\nAtenciosamente,\nEquipe Mauro")

def generate_response(categoria: str, email_texto: str) -> str:
    """
    Gera uma resposta curta e objetiva em pt-BR, adequada à categoria.
    - categoria: 'Produtivo' ou 'Improdutivo'
    - email_texto: conteúdo bruto do e-mail
    Faça um resposta boa para o e-mail que foi digitado.
    """
    policy = f"""
    Faça uma resposta perfeita para oque foi digitado no E-mail.
    Escreva em português do Brasil, profissional e cordial.
    Limite-se a 3–6 frases. Seja direto, sem jargões. Evite prometer prazos específicos.
    Inclua sempre um rodapé de encerramento já fornecido (não reescreva o rodapé).
    "{categoria}".

    Regras por categoria:
    - Produtivo: reconheça a solicitação, confirme entendimento, peça dado pendente (se fizer sentido),
    e informe o próximo passo em termos gerais (ex.: "vamos verificar e retornamos").
    - Improdutivo: agradeça, informe gentilmente que o assunto não demanda ação, e ofereça canal de apoio.

    Conteúdo do e-mail (resuma apenas o essencial, sem copiar dados sensíveis):
    \"\"\"{email_texto[:3000]}\"\"\"  # use apenas o necessário

Formato final:
[corpo de 3–6 frases]
{SIGN_OFF}
"""

    try:
        resp = model.generate_content(policy)
        txt = (resp.text or "").strip()
        # Garantir o rodapé (caso o modelo não obedeça)
        if SIGN_OFF.strip() not in txt:
            txt = txt.rstrip() + SIGN_OFF
        return txt
    except Exception as e:
        # Fallback
        base = (
            "Obrigado pela sua mensagem. "
            "Recebemos seu contato e vamos analisar para retornar com orientações."
            if categoria == "Produtivo"
            else "Obrigado pela sua mensagem. Até o momento, não há ação necessária, mas seguimos à disposição."
        )
        return base + SIGN_OFF