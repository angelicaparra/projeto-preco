import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def gerar_painel():
    sns.set_theme(style="whitegrid")
    caminho_limpos = 'data/limpos'
    
    produtos = {
        'boi_gordo_limpo.csv': ('Boi Gordo', '#2ecc71', 'R$/@'),
        'etanol_limpo.csv': ('Etanol Hidratado', '#e67e22', 'R$/Litro'),
        'leite_limpo.csv': ('Leite (SP)', '#3498db', 'R$/Litro'),
        'ovos_limpo.csv': ('Ovos Brancos (Bastos)', '#f1c40f', 'R$/Caixa')
    }

    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    axes = axes.flatten() 

    for i, (arquivo, info) in enumerate(produtos.items()):
        caminho = os.path.join(caminho_limpos, arquivo)
        
        if os.path.exists(caminho):
            df = pd.read_csv(caminho)
            df['data'] = pd.to_datetime(df['data'])
            
            # Plotagem
            sns.lineplot(ax=axes[i], data=df, x='data', y='preco_reais', 
                         color=info[1], marker='o', linewidth=2.5)
            
            # Títulos e Labels
            axes[i].set_title(f"Tendência: {info[0]}", fontsize=14, fontweight='bold')
            axes[i].set_ylabel(info[2])
            axes[i].set_xlabel("")
            
            # Melhorar a visualização das datas no eixo X
            plt.setp(axes[i].get_xticklabels(), rotation=30)


    plt.tight_layout()
    plt.suptitle("Monitoramento de Preços Agropecuários", fontsize=18, y=1.02, fontweight='bold')
    
    # Salvar o resultado
    plt.savefig('painel_agropecuario.png', bbox_inches='tight', dpi=300)
    print("🚀 Painel gerado com sucesso: painel_agropecuario.png")
    plt.show()

if __name__ == "__main__":
    gerar_painel()