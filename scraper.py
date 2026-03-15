import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def coletar_com_selenium():
    print("Iniciando coleta com Selenium (Abrindo navegador)...")
    
    url = "https://www.cepea.esalq.usp.br/br/indicador/amendoim.aspx"
    
    # Configurações para o Chrome não aparecer (rodar em segundo plano)
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Roda sem abrir a janela
    
    try:
        # Inicializa o navegador
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        driver.get(url)
        time.sleep(5) # Espera 5 segundos para o site carregar tudo
        
       
        html = driver.page_source
        
        
        tabelas = pd.read_html(html)
        driver.quit() # Fecha o navegador

        if tabelas:
            df_precos = tabelas[0]
            if not os.path.exists('data'):
                os.makedirs('data')
            df_precos.to_csv('data/precos_amendoim_bruto.csv', index=False)
            print("✅ SUCESSO! O arquivo CSV foi criado na pasta /data")
            return df_precos.head()
        
    except Exception as e:
        print(f"❌ Erro fatal: {e}")

if __name__ == "__main__":
    resultado = coletar_com_selenium()
    print(resultado)