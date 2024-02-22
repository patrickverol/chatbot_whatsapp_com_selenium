![Chatbot_Whatsapp](https://github.com/patrickverol/chatbot_whatsapp_com_selenium/assets/102604896/15684224-2261-4679-a30c-dbdf5411c858)

<br>
  <h1 align="center">
    Chatbot para Whatsapp
  </h1>
<br/>

<div align="center">
    <a href = "https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" target="_blank"></a> 
    <a href = "https://python-poetry.org/docs/"><img src="https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D" target="_blank"></a>
    <a href = "https://www.selenium.dev/pt-br/documentation/"><img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white" target="_blank"></a>
    <a href = "https://learn.microsoft.com/pt-br/powershell/scripting/overview?view=powershell-7.4"><img src="https://img.shields.io/badge/Powershell-2CA5E0?style=for-the-badge&logo=powershell&logoColor=white" target="_blank"></a>
</div> 

## Sobre o projeto

Neste projeto, utilizo a biblioteca Selenium do Python para abrir o Whatsapp Web e criar um Chatbot. Através de um loop "while" mantenho o selenium capturando a última mensagem enviada pelo usuário, o bot então interage com o usuário através de comandos pré definidos em "/mais", tais comandos acionam funções do python criadas para executar uma ação (podem ser criadas mais funções posteriormente para aumentar o número de funcionalidades do bot). Quando o usuário desejar encerrar a conversa, ele pode digitar "/quit".


## Instalação e configuração

  1. Clone o repositório

```bash
  git clone https://github.com/patrickverol/chatbot_whatsapp_com_selenium
  cd chatbot_whatsapp_com_selenium
```
  2. Insira o número ou nome da pessoa a qual deseja enviar a mensagem:

```bash
  # Abra o arquivo app.py e na linha 109 do código:
  #    -> bot.abre_conversa("Patrick")  # Passando o numero ou o nome do contato
  # Altere o nome Patrick para o nome ou número da pessoa que deseja inicar a conversa.
```
  3. Configure a versão correta do Python com pyenv:

```bash
  pyenv install 3.11.5
  pyenv local 3.11.5
```
  4. Configurar poetry para Python version 3.11.5 e ative o ambiente virtual:

```bash
  poetry env use 3.11.5
  poetry shell
```
  5. Instale as dependências do projeto:

```bash
  poetry install
```
  6. Execute o comando de execucão do programa:

```bash
  task run
```
  7. Acompanhe o funcionamento do Bot através do navegador.

## Contato

Para dúvidas, sugestões ou feedbacks:

<div>
    <a href="https://www.linkedin.com/in/patrick-verol/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
    <a href = "mailto:patrickverol@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
</div> 

