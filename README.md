📈 Monitoramento Agrícola - Foco Alta Paulista
Este projeto automatiza a coleta, processamento e visualização de preços de commodities agrícolas (foco inicial: Boi Gordo) utilizando dados reais do CEPEA/USP. O objetivo é um estudo e aperfeiçoamento em ferramentas de análise.

🚀 Funcionalidades
Web Scraping: Captura de dados em tempo real utilizando Selenium e Chrome WebDriver, configurado para contornar bloqueios de segurança.

Data Cleaning: Tratamento, renomeação de colunas e normalização de tipos de dados (float e datetime) com Pandas.

Data Visualization: Geração de gráficos de tendência automatizados com Matplotlib e Seaborn.

🛠️ Tecnologias Utilizadas
Python 3.x

Pandas (Manipulação de dados)

Selenium (Automação de navegador)

Matplotlib/Seaborn (Visualização)

Webdriver Manager (Gestão de drivers)

📁 Estrutura do Repositório
scraper.py: O "robô" que acessa o site e extrai o HTML.

processor.py: O script que limpa o CSV e prepara para análise.

visualizer.py: O script que gera a imagem do gráfico.

data/: Pasta onde ficam os arquivos de dados (CSV).

exports/: Pasta onde o gráfico final é salvo.

🔧 Como Testar o Projeto
Clone o repositório.

Crie um ambiente virtual: python -m venv venv.

Instale as dependências: pip install -r requirements.txt.

Execute os scripts na ordem: scraper.py -> processor.py -> visualizer.py.

Desenvolvido por Angélica Parra