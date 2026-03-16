import pandas as pd
import os

def processar_dados():
    origem_arquivo = 'data'
    destino_arquivo = 'data/limpos'

    if not os.path.exists(destino_arquivo):
        os.makedirs(destino_arquivo)

    arquivos = [f for f in os.listdir(origem_arquivo) if f.endswith('.csv') and 'limpo' not in f]
    print(f"🧹 Iniciando limpeza personalizada de {len(arquivos)} arquivos...")

    for arquivo in arquivos:
        try:
            caminho_input = os.path.join(origem_arquivo, arquivo)
            df = pd.read_csv(caminho_input, dtype=str)
            nome_prod = arquivo.lower()

           # --- MAPEAMENTO DE COLUNAS BASEADO NO SEU INPUT INICIAL---
            
            if 'boi_gordo' in nome_prod:
                df = df.rename(columns={df.columns[0]: 'data', 'Valor R$*': 'preco_reais'})

            elif 'etanol' in nome_prod:
                # O Etanol tem data "09 - 13/03/2026". Vamos pegar só o "13/03/2026"
                df[df.columns[0]] = df[df.columns[0]].str.split('-').str[-1].str.strip()
                df = df.rename(columns={df.columns[0]: 'data', 'R$/litro': 'preco_reais'})

            elif 'leite' in nome_prod:
                df = df[df['Estado'].str.contains('SP', na=False)].copy()
                meses_pt = {
                    'jan': '01', 'fev': '02', 'mar': '03', 'abr': '04',
                    'mai': '05', 'jun': '06', 'jul': '07', 'ago': '08',
                    'set': '09', 'out': '10', 'nov': '11', 'dez': '12'
                }
                for mes_nome, mes_num in meses_pt.items():
                    df[df.columns[0]] = df[df.columns[0]].str.replace(mes_nome, f"01/{mes_num}", case=False)
                
                df[df.columns[0]] = df[df.columns[0]].str.replace(r'/(\d{2})$', r'/20\1', regex=True)
                df = df.rename(columns={df.columns[0]: 'data', 'Preço médio': 'preco_reais'})

            elif 'ovos' in nome_prod:
                # Filtrando Bastos cidade da região, foco em ovo
                df = df[df['Região'].str.contains('Bastos', na=False)].copy()
                df = df.rename(columns={df.columns[0]: 'data', 'Branco': 'preco_reais'})

            # --- LIMPEZA E FORMATAÇÃO ---
            df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

            # Converter preço (Tratando as vírgulas e pontos)
            if df['preco_reais'].dtype == object:
                df['preco_reais'] = (df['preco_reais']
                                     .str.replace('.', '', regex=False)
                                     .str.replace(',', '.', regex=False))
                
            df['preco_reais'] = pd.to_numeric(df['preco_reais'], errors='coerce')

            # --- Ajuste de Escala ---
            
            # Se o Boi deu 35000, dividimos por 100 para voltar a ser 350.00
            if 'boi_gordo' in nome_prod:
                df['preco_reais'] = df['preco_reais'] / 100
            
            # Se o Etanol deu 29000, dividimos por 10000 para voltar a ser 2.90
            if 'etanol' in nome_prod:
                df['preco_reais'] = df['preco_reais'] / 10000

            # Se o Leite deu 21056, dividimos por 10000 para virar 2.10
            if 'leite' in nome_prod:
                df['preco_reais'] = df['preco_reais'] / 10000
            

            # Remover lixo e ordenar
            # Garantindo que o preço seja tratado como número decimal (float)
            df['preco_reais'] = df['preco_reais'].astype(float)
            df = df.dropna(subset=['data', 'preco_reais'])
            df = df.sort_values('data')

            nome_limpo = arquivo.replace('.csv', '_limpo.csv')
            df[['data', 'preco_reais']].to_csv(
                os.path.join(destino_arquivo, nome_limpo), 
                index=False, 
                encoding='utf-8-sig',
                float_format='%.2f' 
            )

            print(f"✅ {arquivo} finalizado! ({len(df)} linhas)")

        except Exception as e:
            print(f"⚠️ Erro ao processar {arquivo}: {e}")      

    print(f"\n✨ Tudo pronto! Arquivos limpos salvos em: {destino_arquivo}")  

if __name__ == "__main__":
    processar_dados()