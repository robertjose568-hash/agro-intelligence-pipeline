# Agro-Intelligence Pipeline: Da colda ao Campo
Este projeto é uma solução de **Engenharia de dados** coltada para o setor de **Agribusiness**. O objetivo é transformar cotações internacionais complexas em indicadores financeiros simplificados para o produtor rural e gestores do agro.

## O problema
No mercado de commodities, os preços são cotados em Bolsas Internacionais (como Chicago - CBOT) em dólares e unidades de medida entrangeiras (Bushels). Para o produtor brasileiro, entender a viabilidade real da saca em Reais (R$) exige cálsulos constantes de câmbio, conversão de medidas e descontos logícos.

## A solução
Desenvolvi um pipeline automátio que:
1. **Extração (ETL):** Consome dados em tempo real via API das principais commodities (Soja, Milho, Algodão, Café) e paridade cambial (USD/BRL)
2. **Armazenamento:** Estrutura e persiste as informações em um banco de dados **PostgreSQL** rodando em ambiente Linux (WSL)
3. **Inteligência Econômica:** Um algoritmo em Python realiza a conversão automática para o padrão brasileiro (Saca 60kg) e calcula o **Preço Líquido Estimado**
4. **Visualização:** Gera relatórios gráficos automáticos ('.png) para monitoramento de tendências.
5. **Automação:** Sistema configurado via **Crontab** para execução autônoma diária.

## Tecnologias
- **Linguagem:** Python 3.12 (Pandas, SQLALchemy, Matpltlib)
- **Banco de Dados:** PostgreSQL
- **Ambiente:** Linux (Ubuntu/WSL)
- **Ferramentas:** Git, Venv, Crontab

## Exemplo de Saída
o sistema processa os dados e entrega uma análise clara no terminal:
- **Soja Chicago:** US 11.66
- **Valor Bruto Saca (60kg):** R$ 133.95
- **Valor Líquido (Est. com frete/taxas):** R$ 120.55
