import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import io

def coletar_dados_agro():
    produtos = {
        "boi_gordo": "https://www.cepea.esalq.usp.br/br/indicador/boi-gordo.aspx",
        "etanol": "https://www.cepea.org.br/br/indicador/etanol.aspx",
        "mandioca": "https://www.cepea.org.br/br/indicador/mandioca.aspx",
        "ovos": "https://www.cepea.org.br/br/indicador/ovos.aspx",
        "leite": "https://www.cepea.org.br/br/indicador/leite.aspx"
    }
    print("Iniciando coleta com Selenium (Abrindo navegador)...")

    # Configurações para o Chrome abrir para passar pela segurança [Cloudflare]
    chrome_options = Options()
    #chrome_options.add_argument("--headless") 

    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    #não fexar a pagina antes de finalizar a coleta, para evitar bloqueio do Cloudflare
    driver.maximize_window()
    
    if not os.path.exists('data'):
        os.makedirs('data')

    for nome, url in produtos.items():
        try:
            print(f"📡 Coletando dados de: {nome}...")
            driver.get(url)
            time.sleep(10) # Espera o site carregar
            
            html = driver.page_source
            tabelas = pd.read_html(io.StringIO(html))

            if tabelas:
                df = tabelas[0]
                # Salvando cada um com seu nome
                df.to_csv(f'data/{nome}.csv', index=False, encoding='utf-8-sig')
                print(f"✅ {nome} salvo com sucesso!")
            
        except Exception as e:
            print(f"❌ Erro ao coletar {nome}: {e}")
        
    driver.quit()
    print("\n🏁 Coleta finalizada! Todos os arquivos estão na pasta /data")

if __name__ == "__main__":
    coletar_dados_agro()