Projeto ETL de Criptomoedas
Este projeto é um pipeline ETL que coleta dados atualizados de criptomoedas usando a API da CoinGecko, trata os dados com pandas e armazena em um banco MySQL. Tudo isso orquestrado com o Apache Airflow, rodando em containers Docker.

🔧 Tecnologias usadas
Python

Apache Airflow

Docker

MySQL

Pandas

Requests

📦 O que esse projeto faz
Coleta diariamente dados como nome, símbolo, preço, volume, market cap e variação das principais moedas (Bitcoin, Ethereum, Solana, etc)

Padroniza os dados (como nomes e datas) com funções de transformação

Armazena tudo em uma tabela chamada moedas no MySQL

🚀 Como rodar
Clone o repositório

Suba os containers com docker-compose up -d

Acesse o Airflow em localhost:8080

Ative a DAG ETL_coins e veja os dados fluírem 