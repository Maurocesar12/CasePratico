
# 📧 Classificador Inteligente de E-mails (AutoU)

Projeto desenvolvido como parte do processo seletivo para a vaga na AutoU.

---

## 🚀 Objetivo

Criar uma aplicação capaz de **classificar e-mails automaticamente** como:

- ✅ **Produtivo** – exige ação ou resposta
- ❌ **Improdutivo** – não requer resposta (ex: felicitações)

E ainda gerar uma **resposta sugerida com base na categoria**.

---

## 🧠 Inteligência Artificial

Após testes com modelos da Hugging Face (como `tiny-distilroberta-base` e `distilbert-sst-2`), a aplicação final utiliza:

- **Gemini API (Google)**: leve, compatível com Render Free, com melhor desempenho em português
- Modelo local com **Scikit-learn + TF-IDF**, treinado com e-mails reais, usado como fallback (caso queira comparar)

---

## 🖥️ Tecnologias Utilizadas

| Tecnologia     | Finalidade                       |
|----------------|----------------------------------|
| Python + Flask | Backend web                      |
| Bootstrap 5    | Interface moderna e responsiva   |
| Google Gemini  | Classificação com IA             |
| NLTK + Regex   | Pré-processamento do texto       |
| PyMuPDF        | Leitura de arquivos PDF          |

---

## 🌐 Aplicação Online

Acesse a aplicação rodando em produção:

🔗 [https://casepratico.onrender.com](https://casepratico-main.onrender.com/)

---

## 🧪 Como usar

1. Acesse o link da aplicação
2. Insira o conteúdo do e-mail ou envie um arquivo `.txt` ou `.pdf`
3. Clique em **“Classificar”**
4. Veja a **categoria** e a **resposta sugerida** pela IA

---

## 📁 Estrutura do Projeto

```
📦 project-root
├── app.py                 # Arquivo principal Flask
├── requirements.txt       # Dependências
├── templates/index.html   # Interface com Bootstrap
├── utils/
│   ├── classifier.py      # Classificador (IA + fallback local)
│   └── preprocess.py      # Limpeza do texto
├── model/
│   ├── email_classifier.pkl
│   └── vectorizer.pkl
```
---

## ⚙️ Instalação na sua máquina

Siga os passos abaixo para rodar o projeto no seu computador:

### 1. Pré-requisitos
- **Python 3.9+** instalado ([download aqui](https://www.python.org/downloads/))
- Conta no [Google AI Studio](https://ai.google.dev/) para gerar sua **API Key do Gemini**

### 2. Clonar o repositório
```bash
git clone https://github.com/usuario/CasePratico.git
cd CasePratico/CasePratico-main
```
### 3. Para iniciar o projeto
```bash
- pip install -r requirements.txt

- python app. py
```
---

## 📋 Observações Finais

- A solução foi criada com foco em **simplicidade, desempenho e experiência de uso**
- A IA está conectada em produção, mas o código está preparado para fallback com modelo local
- A interface foi construída com atenção à usabilidade e estética
- O projeto foi testado em `.txt`, `.pdf` e entradas diretas

---

## 🤝 Contato

**Mauro César**  
Candidato à vaga de Engenheiro de Software Júnior  
📧 mauro.guimaraes@segna.com.br 
🔗 [LinkedIn](https://www.linkedin.com/in/mauro-c%C3%A9sar-guimaraes-santos-junior-b9638b203/)

---
