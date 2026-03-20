import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
import logging

# Configuração de avisos no terminal
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def obter_conexao():
    # Conexão direta que já validamos que funciona no seu Ubuntu
    return create_engine('postgresql://postgres:admin123@localhost:5432/postgres')

def pipeline_agro_financeiro():
    tickers = ["SLCE3.SA", "AGRO3.SA", "SMTO3.SA"]
    engine = obter_conexao()
    
    try:
        logger.info("Coletando cotações da B3...")
        # Download simples para evitar erros de estrutura
        dados = yf.download(tickers, period="5d", interval="15m")
        
        if dados.empty:
            print("Erro: Yahoo Finance não retornou dados.")
            return

        # Organizando os dados de forma simples para o banco
        df_fechamento = dados['Close'].reset_index()
        df_final = df_fechamento.melt(id_vars=['Datetime'], var_name='ticker', value_name='preco')
        df_final.columns = ['data_hora', 'ativo', 'valor']
        df_final = df_final.dropna()

        logger.info(f"Conectando ao banco e salvando {len(df_final)} linhas...")
        df_final.to_sql('monitoramento_financeiro', engine, if_exists='append', index=False)
        print("SUCESSO: Dados financeiros integrados!")

    except Exception as e:
        print(f"Erro no processo: {e}")

if __name__ == "__main__":
    pipeline_agro_financeiro()