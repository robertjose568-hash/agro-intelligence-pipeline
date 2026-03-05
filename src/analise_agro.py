from sqlalchemy import create_engine
import pandas as pd

# Conexão com o Banco
engine = create_engine('postgresql://postgres:admin123@localhost:5432/postgres')

def calcular_viabilidade():
    # Lê os dados do banco
    df = pd.read_sql('SELECT * FROM commodities', engine)

    #Pega o último dólar salvo (Filtra pelo nome exato que está no dicionário)
    dolar = df[df['produto'] == 'Dólar'] ['valor'].iloc[-1]

    print("/n" + "="*45)
    print("RELATÓRIO DE INTELIGÊNCIA ECONÔMIA AGRO")
    print("="*45)

    # Configurações de Conversão
    # Fator para transformar a unidade da Bolsa em Saca de 60kg no Brasil
    configs = {
        'Soja': 2.2046, # Bushel -> Saca 60kg
        'Milho': 2.3621, # Bushel -> Saca 60kg
        'Cafe': 1.3227, # Bushel -> Saca 60kg
        'Trigo': 2.2046, # Bushel -> Saca 60kg
        'Algodao': 1.0 # Valor de referência (ajustável para Arroba)
    }

    for produto, fator in configs.items():
        try:
            #Filtra o último preço em dólar do produto
            preco_usd = df[df['produto'] == produto] ['valor'].iloc[-1]

            #Cálculo Econômico Final
            valor_bruto_brl = preco_usd * fator * dolar
            valor_liquido = valor_bruto_brl * 0.90 # Desconto de 10% (Basis/Frete)

            print(f"{produto.upper()}:")
            print(f"Chicago/NY: U$ {preco_usd:.2f}")
            print(f"Saca Líquida: R$ {valor_liquido:.2f}")
            print("-" * 30)
        except Exception as e:
            continue

if __name__ == "__main__":
    calcular_viabilidade()