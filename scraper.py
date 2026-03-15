import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import io

def coletar_com_selenium():
    print("Iniciando coleta com Selenium (Abrindo navegador)...")
    
    url = "https://www.cepea.esalq.usp.br/br/indicador/boi-gordo.aspx"

    # Configurações para o Chrome abrir para passar pela segunrança
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)
        time.sleep(5)
       
        html = driver.page_source

        tabelas = pd.read_html(io.StringIO(html))
        driver.quit() 

        if tabelas:
            df_precos = tabelas[0]
            if not os.path.exists('data'):
                os.makedirs('data')
            df_precos.to_csv('data/boi_gordo.csv', index=False, encoding='utf-8-sig')
            print("✅ SUCESSO! O arquivo CSV foi criado na pasta /data")
            return df_precos.head()
        
    except Exception as e:
        print(f"❌ Erro fatal: {e}")

if __name__ == "__main__":
    resultado = coletar_com_selenium()
    print(resultado)