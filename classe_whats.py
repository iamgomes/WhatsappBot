from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import keyboard
import time

class WhatsappBot:
    def __init__(self):
        self.grupo_ou_pessoa = input("\nDIGITE O NOME DO GRUPO OU PESSOA DE ONDE VOCÊ DESEJA BAIXAR OS ARQUIVOS: ")
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        print('Abrindo o navegador...')
        self.driver = webdriver.Chrome(
            executable_path=r'./src/chromedriver.exe', chrome_options=options)
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)


    def BaixarArquivos(self):
        campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{self.grupo_ou_pessoa}']")
        campo_grupo.click()

        element = self.driver.find_element_by_class_name('_33LGR')
        element.click()

        time.sleep(2)

        while True:
            time.sleep(5)
            if keyboard.is_pressed('esc'):
                print('\nVALEU! ATÉ A PRÓXIMA :)')
                break
            else:
                try:
                    botao_download = self.driver.find_element_by_xpath("//span[@data-icon='audio-download']")
                    botao_download.click()
                    print('Baixando arquivo...')
                    time.sleep(2)
                    element.send_keys(Keys.PAGE_UP)
                except:
                    print('Nenhum arquivo nesta parte...')
                    element.send_keys(Keys.PAGE_UP)
                    continue