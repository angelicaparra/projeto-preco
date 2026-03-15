import pandas as pd
import os

def processar_dados():
    caminho_arquivo = 'data/boi_gordo.csv'

    if not os.path.exists(caminho_arquivo):
        print("❌ Arquivo CSV não encontrado. Por favor, execute o scraper primeiro.")
        return

    df = pd.read_csv(caminho_arquivo)
    df.columns = ['data', 'preco_reais', 'var_dia', 'var_mes', 'preco_dolar']

    # Nota: O CEPEA às vezes traz o valor multiplicado por 100 ou com vírgula.
    # Tratando para que seja um número real.
    df['preco_reais'] = df['preco_reais'].astype(float) / 100

    #convertendo a coluna de data para o formato datetime
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')

    # Salvando o arquivo limpo
    df.to_csv('data/boi_gordo_limpo.csv', index=False, encoding='utf-8-sig')

    print("✨ Dados processados e salvos em 'data/boi_gordo_limpo.csv'!")
    print(df.head())

if __name__ == "__main__":
    processar_dados()