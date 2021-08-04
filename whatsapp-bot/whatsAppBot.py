from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#from chatter import getBotResponse
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import os

class wspBot:
    def __init__(self):
        self.dir_path = os.getcwd()
        self.driver = webdriver.Chrome("C://Drivers//chromedriver.exe")
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r"user-data-dir="+self.dir_path+"\profile\wpp")
        #self.options.add_argument('--headless')
        self.response = ""
        
        self.driver = webdriver.Chrome(options=self.options)
        self.openWhatsappWeb()
        
    
    def openWhatsappWeb(self):
        
        self.driver.get('https://web.whatsapp.com')
        self.driver.implicitly_wait(15)
        return True

    def chamaJarvis(self):
        messages = self.driver.find_elements_by_xpath("//div[@class='JnmQF _3QmOg']//div[@class='_2aBzC']//div[@class='TbtXF']//div[@class='_1SjZ2']")

        try:
            for i in messages:
                if i.text == 'BOT':
                    i.click()
                    sleep(1)
                    return True
        except:
            return False

    def escuta(self):
        try:
            post = self.driver.find_elements_by_xpath("//div[@class='_3XpKm _20zqk']")
            ultimo = len(post) - 1
            texto = post[ultimo].find_element_by_css_selector('span.selectable-text').text
        except:
            texto = ''
        return texto

    def responde(self, texto):
        if texto == 'start':
            response = 'Olá, como posso ajudar? Não liga, eu sou meio burro, mas estou aprendendo... Diga "sair" para parar. :)'
        else:
            response = self.get_response(texto)
            #response = getBotResponse(texto)
        response = str(response)
        self.response = 'bot: ' + response

        self.caixa_de_mensagem = self.driver.find_element_by_class_name('_2A8P4')
        self.caixa_de_mensagem.send_keys(self.response)
        sleep(1)
        self.botao_enviar = self.driver.find_element_by_xpath('//div[@class="EBaI7"]')

        button = self.driver.find_element_by_xpath('//div[@class="EBaI7"]')

        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(button).click(button).perform()

    def get_response(self, texto):
        if texto == 'start':
            message = 'Olá, como posso ajudar? Diga "sair" para parar. :)'

        else:
            message = "Ainda estou aprendendo"
        
        return message

    def sair(self, texto):
        self.response = 'bot: Ate breve. :)'

        self.caixa_de_mensagem.send_keys(self.response)
        self.botao_enviar.click()
        self.runBot()
        

    def runBot(self):
        while not self.chamaJarvis():
            self.chamaJarvis()

        self.driver.implicitly_wait(15)
        self.responde('start')
        
        ultimo_texto = ''

        while True:
            texto = self.escuta()
            if texto != ultimo_texto and texto != self.response:
                ultimo_texto = texto
                texto = texto.lower()
                
                if texto == 'sair':
                    self.sair(texto)
                    sleep(1)
                    break
                else:
                    self.responde(texto)

go = wspBot().runBot()
