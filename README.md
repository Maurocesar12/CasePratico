## Contexto do Desafio

Estamos criando uma **solução digital para uma grande empresa** do setor financeiro que lida com um **alto volume de emails diariamente**. Esses emails podem ser mensagens solicitando um status atual sobre uma requisição em andamento, compartilhando algum arquivo ou até mesmo mensagens improdutivas, como desejo de feliz natal ou perguntas não relevantes. 

Nosso **objetivo é automatizar a leitura e classificação desses emails** e sugerir classificações e respostas automáticas de acordo com o teor de cada email recebido, **liberando tempo da equipe** para que não seja mais necessário ter uma pessoa fazendo esse trabalho manualmente.

## Objetivo do Desafio Simplificado

Desenvolver uma aplicação web simples que utilize inteligência artificial para:

1. **Classificar** emails em categorias predefinidas.
2. **Sugerir respostas automáticas** baseadas na classificação realizada.

**Categorias de Classificação**

- **Produtivo:** Emails que requerem uma ação ou resposta específica (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema).
- **Improdutivo:** Emails que não necessitam de uma ação imediata (ex.: mensagens de felicitações, agradecimentos).

## Requisitos do Projeto

**1. Interface Web (HTML)**

**Formulário de Upload:**

- Permitir o upload de arquivos de email em formatos .txt ou .pdf ou a inserção direta de texto de emails.
- Botão para enviar o documento/email para processamento.

**Exibição dos Resultados:**

- Mostrar a categoria atribuída ao email (Produtivo ou Improdutivo).
- Exibir a resposta automática sugerida pelo sistema.

*Pro-tip:* a interface é uma ótima oportunidade para você se destacar, trazendo elementos visuais bem pensados, funcionalidades úteis, recursos mais avançados e uma experiência que realmente encante o usuário final.

**2. Backend em Python**

**Leitura e Processamento:**

- Desenvolver um script em Python que leia o conteúdo dos emails enviados.
- Utilizar técnicas de processamento de linguagem natural (NLP) para pré-processar o texto (remoção de stop words, stemming/lemmatização, etc.).

**Classificação e Resposta:**

- Implementar um algoritmo de classificação que categorize o conteúdo em **Produtivo** ou **Improdutivo**.
- Utilizar uma API de AI (como Hugging Face Transformers, OpenAI GPT, ou outra de sua preferência) para:

**Classificação:**

- Determinar a categoria do email.

**Geração de Resposta:**

- Sugerir uma resposta automática adequada à categoria identificada.

**Integração com a Interface Web:**

- Conectar o backend com a interface HTML para receber entradas e exibir resultados.

**3. Hospedagem na Nuvem**

**Deploy da Aplicação:**

- Hospedar a aplicação web em uma plataforma de nuvem gratuita (como Heroku, Vercel, AWS Free Tier, Google Cloud Platform, etc.) e disponibilizar um link online e funcional para que o time da AutoU ou usuários externos possam acessar e testar o funcionamento da solução.
- Fornecer o link para a aplicação hospedada junto com a submissão do desafio.