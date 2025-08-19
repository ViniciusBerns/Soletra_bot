# 🤖 Automação do jogo "Soletra" (G1 Jogos)

Este projeto tem como objetivo **automatizar o jogo diário "Soletra"**, disponível no [G1 Jogos](https://g1.globo.com/jogos/soletra/).  
Usando **Python + Selenium**, o script lê uma lista de palavras de um arquivo JSON e as insere automaticamente no campo de resposta do jogo.

---

## 📌 Como funciona

1. **Extração das palavras**  
   - O script abre o arquivo `soletra.json`, que contém uma lista de palavras no formato:
     ```json
     {
       "word_list": [
         {"word": "exemplo1"},
         {"word": "exemplo2"},
         {"word": "exemplo3"}
       ]
     }
     ```
   - Este arquivo `soletra.json` foi obtido diretamente do **site do jogo**, por meio da ferramenta de inspeção do navegador.
   - A função `extract_words` percorre esse arquivo e cria uma lista somente com as palavras.

2. **Abertura do jogo**  
   - O Selenium abre o navegador Chrome na página do jogo **Soletra**.
   - O script interage com os botões iniciais (entrar e fechar tutoriais/popups).

3. **Inserção automática**  
   - Para cada palavra extraída do JSON:
     - Digita no campo de resposta.
     - Pressiona **Enter** para validar.
     - Aguarda um pequeno intervalo antes de passar para a próxima palavra.

4. **Finalização**  
   - Após inserir todas as palavras, o navegador é fechado automaticamente.

---

## 🛠️ Tecnologias utilizadas
- [Python 3](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [Chrome WebDriver](https://chromedriver.chromium.org/)

## AVISO
- Este projeto foi feito exclusivamente para prática e uso educacional

---

## ▶️ Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/soletra-bot.git
   cd Soletra_bot



