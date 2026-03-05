import yfinance as yf
from sqlalchemy import create_engine
import pandas as pd

#Conexão com o Banco
engine = create_engine('postgresql://postgres:admin123@localhost:5432/postgres')

def salvar_dados_mercado():
    print("Coletando dados da B3 e Chicago...")
    #Buscando Soja, Milho e Dólar
    ativos = {
        "Soja": "ZS=F",
        "Milho": "ZC=F",
        "Algodao": "CT=F",
        "Cafe": "KC=F",
        "Trigo": "ZW=F",
        "Dólar": "USDBRL=X"
        }

    lista_precos = []
    for nome, ticker in ativos.items():
        preco = yf.Ticker(ticker).history(period="1d") ['Close'].iloc[-1]
        # Ajuste de escala
        if "USD" not in ticker:
            preco = preco / 100
        
        lista_precos.append({"produto": nome, "valor": round(preco, 4)})
    
    df = pd.DataFrame(lista_precos)

    #Salvar direto no SQL
    df.to_sql('commodities', engine, if_exists='append', index=False)
    print("Dados salvos com sucesso no PostgreSQL!")

if __name__ == "__main__":
    salvar_dados_mercado()