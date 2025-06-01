<img
  src="./static/img/_banner.png"
  alt="AI Evaluation"
  style="width: 100%"
/>

**AI Evaluation** é uma aplicação dedicada à análise comparativa de imagens geradas por diferentes IAs. Para isso, quatro modelos distintos foram selecionados: ChatGPT, Google Gemini, Runware (Civitai) e Stability AI. Cada um deles cria imagens a partir do mesmo prompt, e cabe a você avaliar qual foi o melhor, por meio do seu voto.

Após a avaliação, os resultados ficam disponíveis para visualização, mostrando quais serviços tiveram o melhor desempenho. Além disso, você pode comparar sua avaliação com a do próprio ChatGPT, que também analisa as imagens geradas — inclusive as que ele mesmo criou.

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

### 🛠️ Instalação e Execução

A aplicação foi desenvolvida em **Python 3.12**, recomendando-se o uso dessa versão para garantir compatibilidade. Para configurar a aplicação, siga estas instruções a partir do diretório raiz do projeto.

#### 1️⃣ Configurar as Variáveis de Ambiente

Antes de instalar e executar a aplicação, é necessário configurar as chaves de acesso aos serviços de IA como variáveis de ambiente. Para isso, crie um arquivo `.env`, com base no `.env.example`, e atribua os valores de `GEMINI_AI_KEY`, `OPEN_AI_KEY`, `RUNWARE_KEY` e `STABILITY_AI_KEY`.

#### 2️⃣ Instalar as Dependências

```bash
pip install -r requirements.txt
```

#### 3️⃣ Executar a Aplicação

```bash
python -m app
```

As imagens são geradas durante a primeira inicialização do servidor, o que causa um tempo de espera maior. Esse processo ocorre apenas uma vez, a menos que a base de dados seja apagada.

### 🤝 Doação

Gostou do projeto e gostaria de apoiar financeiramente? Você pode contribuir via **PayPal** ou através do **Pix** — é só clicar em uma das opções abaixo:

[![PayPal](https://img.shields.io/badge/PayPal-Donate-1040C1?labelColor=121661&style=for-the-badge&logo=paypal&link=https://www.paypal.com/donate/?hosted_button_id=2P9HPGUP7Z43S)](https://www.paypal.com/donate/?hosted_button_id=2P9HPGUP7Z43S)
&nbsp;
[![Pix](https://img.shields.io/badge/Pix-Doar-FBB88A?labelColor=F26722&style=for-the-badge&logo=pix&logoColor=ffffff&link=https://tipa.ai/davidsantana06)](https://tipa.ai/davidsantana06)

Este e outros projetos disponíveis no meu perfil foram desenvolvidos de forma independente. Qualquer apoio para manter este propósito é mais do que bem-vindo! 💪

### ⚖️ Licença

Este projeto utiliza a **Licença MIT**, que permite que você use e modifique o código como desejar. O único requisito é dar o devido crédito, reconhecendo o esforço e o tempo dedicados à sua construção.
