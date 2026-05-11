from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import time


class Navegador:

    def iniciar(self):

        # CONFIGURAÇÕES DO CHROME
        options = Options()

        options.add_argument("--start-maximized")

        options.add_argument("--disable-notifications")

        options.add_argument("--disable-infobars")

        options.add_argument("--disable-dev-shm-usage")

        options.add_argument("--disable-blink-features=AutomationControlled")

        # INICIA NAVEGADOR
        driver = webdriver.Chrome(
            options=options
        )

        # ABRIR SITE
        driver.get("https://google.com")

        print("Navegador iniciado com sucesso!")

        # ESPERA
        time.sleep(5)

        # FECHAR
        driver.quit()