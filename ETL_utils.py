import pandas as pd

def limpar_data(data):
    if data is None or data == "":
        return None
    try:
        return pd.to_datetime(data, errors='raise')
    except Exception:
        return None
    
def padronizar_nome_moeda(nome_moeda):
    if nome_moeda is None or nome_moeda == "":
        return None
    return nome_moeda.strip().capitalize()


def padronizar_preco(preco):
    try:
        return pd.to_numeric(preco, errors='coerce')
    except Exception:
        return None


def padronizar_volume(volume):
    try:
        return pd.to_numeric(volume, errors='coerce')
    except Exception:
        return None







    

