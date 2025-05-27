from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd
from ETL_utils import limpar_data, padronizar_nome_moeda, padronizar_preco, padronizar_volume
from database import engine

def coletar_moedas(ti):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum,solana,chainlink,tether"
    }
 
    response = requests.get(url, params=params)
    moedas = response.json()

    df = pd.DataFrame([{
        "moeda": m["name"],
        "simbolo": m["symbol"],
        "preco_usd": m["current_price"],
        "market_cap_usd": m["market_cap"],
        "volume_usd": m["total_volume"],
        "variacao_24h": m["price_change_percentage_24h"],
        "data_coleta": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    } for m in moedas])

    return df

def transformar_dados(ti):
    
    df = ti.xcom_pull(task_ids= "coletar_moedas")

    df = pd.DataFrame(df)

    df['moeda'] = df['moeda'].apply(padronizar_nome_moeda)
    df['data_coleta'] = df['data_coleta'].apply(limpar_data)
    df['preco_usd'] = df["preco_usd"].apply(padronizar_preco)
    df['volume_usd'] = df["volume_usd"].apply(padronizar_volume)

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    return df

def carregar_dados(ti):

    df = ti.xcom_pull(task_ids= "transformar_dados")

    df = pd.DataFrame(df)

    df.to_sql("moedas", con=engine, if_exists="append", index=False)


with DAG(
    dag_id="ETL_coins",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:
    
    extract = PythonOperator(
        task_id= "coletar_moedas",
        python_callable = coletar_moedas
    )

    transform = PythonOperator(
        task_id = "transformar_dados",
        python_callable = transformar_dados
    )

    load = PythonOperator(
        task_id = "carregar_dados",
        python_callable = carregar_dados
    )

extract >> transform >> load