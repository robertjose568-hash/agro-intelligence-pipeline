import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:admin123@localhost:5432/postgres')
df = pd.read_sql('SELECT produto, valor FROM commodities', engine)

# Criar o gráfico
df.plot(kind='bar', x='produto', y='valor', color='green', legend=False)
plt.title('Monitoramento de Ativos - Robert Agro')
plt.ylabel('Preço (Moeda Original)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('relatorio_mercado.png')
print("Gráfico gerado com sucesso: relatorio_mercado.png")
