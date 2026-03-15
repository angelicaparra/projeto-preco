import pandas as pd
import os
import io

def processar_dados():
    origem_arquivo = 'data'
    destino_arquivo = 'data/limpos'

    if not os.path.exists(destino_arquivo):
        os.makedirs(destino_arquivo)

    arquivos = [f for f in os.listdir(origem_arquivo) if f.endswith('.csv') and 'limpo' not in f]
    print(f"🧹 Iniciando limpeza de {len(arquivos)} arquivos...")

    for arquivo in arquivos:
        try:
            caminho_input = os.path.join(origem_arquivo, arquivo)
            df = pd.read_csv(caminho_input)

            # Nota: O CEPEA às vezes traz o valor multiplicado por 100 ou com vírgula.
            # Tratando para que seja um número real.
            colunas_originais = df.columns.tolist()
            df = df.rename(columns={
                colunas_originais[0]: 'data',
                colunas_originais[1]: 'preco_reais'
            })
            #convertendo a coluna de data
            df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

            # Removendo pontos de milar e trocar vírgula por ponto 
            if df['preco_reais'].dtype == object:
                df['preco_reais'] = df['preco_reais'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
            
            df['preco_reais'] = pd.to_numeric(df['preco_reais'], errors='coerce')

            # Garantinhdo que não haja valores nulos
            df = df.dropna(subset=['data', 'preco_reais'])

            nome_limpo = arquivo.replace('.csv', '_limpo.csv')
            df[['data', 'preco_reais']].to_csv(os.path.join(destino_arquivo, nome_limpo), index=False, encoding='utf-8-sig')

            print(f"✅ {arquivo} processado!")

        except Exception as e:
            print(f"⚠️ Erro ao processar {arquivo}: {e}")      

    print(f"\n✨ Tudo pronto! Arquivos limpos salvos em: {destino_arquivo}")  

if __name__ == "__main__":
    processar_dados()