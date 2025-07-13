<img
  src="./static/img/_banner.png"
  alt="AI Evaluation"
  style="width: 100%"
/>

**AI Evaluation** é uma aplicação dedicada à análise comparativa de imagens geradas por diferentes IAs. Para isso, quatro modelos distintos foram selecionados. Cada um deles cria imagens a partir do mesmo prompt, e cabe a você avaliar qual foi o melhor, por meio do seu voto.

Após a avaliação, os resultados ficam disponíveis para visualização, mostrando quais serviços tiveram o melhor desempenho. Além disso, você pode comparar sua avaliação com a do próprio ChatGPT, que também analisa as imagens geradas.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)

![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bulma](https://img.shields.io/badge/bulma-00D0B1?style=for-the-badge&logo=bulma&logoColor=white)

![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
![Google Gemini](https://img.shields.io/badge/google%20gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)
![Runware (Civitai)](<https://img.shields.io/badge/Runware%20(Civitai)-0c4ede?style=for-the-badge>)
![Stability AI](https://img.shields.io/badge/Stability%20AI-7000E0?style=for-the-badge)

![Font Awesome](https://img.shields.io/badge/Font_Awesome-%23FFFFFF.svg?style=for-the-badge&logo=fontawesome&logoColor=528DD7)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## 💡 Modelos de IA Selecionados

| Plataforma   | Modelo(s)                                   | Documentação                                                                                               |
| ------------ | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| OpenAI       | `dall-e-3` e `gpt-4.1`                      | [platform.openai.com/docs/overview](https://platform.openai.com/docs/overview)                             |
| Google AI    | `gemini-2.0-flash-preview-image-generation` | [ai.google.dev/gemini-api/docs](https://ai.google.dev/gemini-api/docs)                                     |
| Runware      | `civitai`                                   | [runware.ai/docs/en/getting-started/introduction](https://runware.ai/docs/en/getting-started/introduction) |
| Stability AI | `stable-image-core`                         | [platform.stability.ai/docs/getting-started](https://platform.stability.ai/docs/getting-started)           |

<sub>Os modelos e suas documentações podem ser atualizados após a construção do projeto. As informações apresentadas são referentes ao período de junho de 2025.</sub>

## 🛠️ Instalação e Execução

A aplicação foi desenvolvida em **Python 3.10**, recomendando-se o uso dessa versão para garantir compatibilidade. Para configurá-la, siga estas instruções a partir do diretório raiz do projeto.

### 1️⃣ Configurar as Variáveis de Ambiente

Antes de instalar e executar a aplicação, é necessário configurar as chaves de acesso aos serviços de IA como variáveis de ambiente. Para isso, crie um arquivo `.env`, com base no `.env.example`, e atribua os valores de `GEMINI_KEY`, `OPENAI_KEY`, `RUNWARE_KEY` e `STABILITY_AI_KEY`.

### 2️⃣ Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Executar a Aplicação

```bash
python -m app
```

<sub>As imagens são geradas durante a primeira inicialização do servidor, o que causa um tempo de espera maior. Esse processo ocorre apenas uma vez, a menos que a base de dados seja apagada.</sub>

## 🚀 Fluxo de Funcionamento

A aplicação funciona por meio de três etapas principais que ocorrem sequencialmente e são interdependentes.

### 🖼️ Geração das Imagens

Na primeira execução da aplicação, o arquivo `generation_entries.json` é lido para resgatar os atributos `group`, `theme` e `prompt`. A partir dessas informações, são feitas requisições para cada serviço de IA em ordem aleatória. As imagens geradas são salvas no banco de dados SQLite, situado na raiz do projeto, e armazenadas como arquivos PNG no diretório `static/img`.

Se o banco de dados apresentar registros de imagem, essa etapa é ignorada em execuções futuras.

### 🤖 Avaliação do ChatGPT

Após a geração, as imagens são avaliadas pelo ChatGPT. Elas são agrupadas e enviadas sem o nome do modelo gerador, contendo apenas o identificador e o conteúdo binário. Para cada grupo, uma imagem é escolhida como a melhor, e o resultado é registrado no banco de dados.

Essa etapa também é ignorada em execuções futuras, caso já exista algum registro de avaliação feita pelo ChatGPT.

### 👤 Avaliação do Usuário

Com as imagens e avaliações do ChatGPT prontas, o usuário pode acessar a interface da aplicação e votar nas melhores imagens por prompt. O processo é intuitivo e ao final é possível visualizar:

- Quantidade de votos por IA (ChatGPT e usuário);
- Tamanho total e médio das imagens por IA;
- Tempo total e médio de geração por IA.

## 🤝 Doação

Gostou do projeto e gostaria de apoiar financeiramente? Você pode contribuir via **PayPal** ou através do **Pix** — é só clicar em uma das opções abaixo:

[![PayPal](https://img.shields.io/badge/PayPal-Donate-1040C1?labelColor=121661&style=for-the-badge&logo=paypal&link=https://www.paypal.com/donate/?hosted_button_id=2P9HPGUP7Z43S)](https://www.paypal.com/donate/?hosted_button_id=2P9HPGUP7Z43S)
&nbsp;
[![Pix](https://img.shields.io/badge/Pix-Doar-FBB88A?labelColor=F26722&style=for-the-badge&logo=pix&logoColor=ffffff&link=https://tipa.ai/davidsantana06)](https://tipa.ai/davidsantana06)

Este e outros projetos disponíveis no meu perfil foram desenvolvidos de forma independente. Qualquer apoio para manter este propósito é mais do que bem-vindo! 💪

## ⚖️ Licença

Este projeto utiliza a **Licença MIT**, que permite que você use e modifique o código como desejar. O único requisito é dar o devido crédito, reconhecendo o esforço e o tempo dedicados à sua construção.
