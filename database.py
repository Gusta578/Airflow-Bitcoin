from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
Base = declarative_base()

usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
porta = os.getenv("PORTA")
banco = os.getenv("BANCO")

engine = create_engine(F"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}")

try:
    with engine.connect() as conexao:
        print("Conexão bem sucedida!")
except Exception as e:
    print(f"A conexão falhou, erro: {e}")
