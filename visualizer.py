import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def gerar_grafico():
    caminho_arquivo = 'data/boi_gordo_limpo.csv'
    
    if not os.path.exists(caminho_arquivo):
        print("❌ Arquivo limpo não encontrado! Rode o processor.py primeiro.")
        return


    df = pd.read_csv(caminho_arquivo)
    df['data'] = pd.to_datetime(df['data'])
    
    # Ordenar os dados por data (caso venha invertido do site)
    df = df.sort_values('data')

    #estilo do grafico
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(12, 6))

    plot = sns.lineplot(data=df, x='data', y='preco_reais', marker='o', color='#2c3e50', linewidth=2.5)

    plt.title('Tendência de Preços: Boi Gordo (CEPEA)', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Data da Coleta', fontsize=12)
    plt.ylabel('Preço (R$)', fontsize=12)
    
    # Rotacionando as datas no eixo X para não ficarem amontoadas
    plt.xticks(rotation=45)

    # Salvando o gráfico em alta resolução
    if not os.path.exists('exports'):
        os.makedirs('exports')
        
    plt.tight_layout()
    plt.savefig('exports/grafico_precos.png', dpi=300)
    
    print("📊 GRÁFICO GERADO! Verifique a pasta 'exports/grafico_precos.png'")
    plt.show()

if __name__ == "__main__":
    gerar_grafico()