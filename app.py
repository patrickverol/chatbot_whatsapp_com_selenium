# Importando as bibliotecas
import os
import random
import time
import warnings

warnings.filterwarnings("ignore")

# Biblotecas para importar o ChromeDriver e verificar a versão
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Bibliotecas para utilizar os comandos Keys e By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class zapbot:

    # O local de execução do nosso script
    dir_path = os.getcwd()
    # Verificando a versão do ChromeDriver
    servico = Service(ChromeDriverManager().install())
    # Caminho onde será criada pasta profile
    profile = os.path.join(dir_path, "wpp")

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        # Configurando a pasta profile, para mantermos os dados da seção
        self.options.add_argument(r"user-data-dir={}".format(self.profile))
        # Inicializa o webdriver
        self.driver = webdriver.Chrome(service=self.servico, options=self.options)
        # Abre o whatsappweb
        self.driver.get("https://web.whatsapp.com/")
        # Aguarda alguns segundos para validação manual do QrCode
        self.driver.implicitly_wait(30)

    def abre_conversa(self, contato):
        """Abre a conversa com um contato especifico"""
        try:
            # Seleciona a caixa de pesquisa de conversa
            self.caixa_de_pesquisa = self.driver.find_element(
                By.CLASS_NAME, "copyable-text"
            )
            # Digita o nome ou numero do contato
            self.caixa_de_pesquisa.send_keys(contato)
            time.sleep(2)
            # Seleciona o contato
            self.contato = self.driver.find_element(
                By.XPATH, "//span[@title = '{}']".format(contato)
            )
            # Entra na conversa
            self.contato.click()
        except Exception as e:
            raise e

    def envia_msg(self, msg):
        """Envia uma mensagem para a conversa aberta"""
        try:
            time.sleep(2)
            # Seleciona acaixa de mensagem, Digita a mensagem
            self.driver.find_element(
                By.XPATH, '//*[@title="Digite uma mensagem"]'
            ).send_keys(msg)
            time.sleep(1)
            # Seleciona botão enviar
            self.botao_enviar = self.driver.find_element(By.CLASS_NAME, "_3XKXx")
            # Envia msg
            self.botao_enviar.click()
            time.sleep(2)
        except Exception as e:
            print("Erro ao enviar msg", e)

    def envia_media(self, fileToSend):
        # Envia media
        try:
            # Seleciona input
            attach = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
            # Adiciona arquivo
            attach.send_keys(fileToSend)
            time.sleep(3)
            # Seleciona botão enviar
            send = self.driver.find_element(By.XPATH, "//span[@data-icon='send']")
            # Clica no botão enviar
            send.click()
        except Exception as e:
            print("Erro ao enviar media", e)

    def ultima_msg(self):
        """Captura a ultima mensagem da conversa"""
        try:
            post = self.driver.find_elements(By.CLASS_NAME, "_21Ahp")
            ultimo = len(post) - 1
            # O texto da ultima mensagem
            texto = (
                post[ultimo].find_element(By.CSS_SELECTOR, "span.selectable-text").text
            )
            return texto
        except Exception as e:
            print("Erro ao ler msg, tentando novamente!")


if __name__ == "__main__":
    bot = zapbot()  # Inicia o objeto zapbot
    bot.abre_conversa("Patrick")  # Passando o numero ou o nome do contato
    bot.envia_msg("Olá, sou o bot whatsapp! Para receber ajuda digite: /help")
    imagem = os.path.join(
        bot.dir_path, "data", f"{str(random.randint(1, 4))}.jpg"
    )  # Passando o caminho da imagem que será enviada
    msg = ""  # Criando a variável msg
    while msg != "/quit":
        time.sleep(1)
        msg = bot.ultima_msg()  # A cada loop recebe a ultima mensagem da conversa
        if msg == "/help":  # Retorna uma mensagem de ajuda
            bot.envia_msg(
                """Bot: Esse é um texto com os comandos válidos:
                /help (para ajuda)
                /mais (para saber mais)
                /quit (para sair)
                """
            )
        elif msg == "/mais":  # Retorna a imagem que selecionamos
            bot.envia_media(imagem)
        elif msg == "/quit":  # Encerra o programa
            bot.envia_msg("Bye bye!")
