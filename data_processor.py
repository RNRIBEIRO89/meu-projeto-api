import pandas as pd
import os
from datetime import datetime

def save_dataframe(df, filename, output_dir):
    """
    Salva um DataFrame em CSV e JSON no diretório de saída, adicionando data/hora à nomenclatura.
    
    :param df: DataFrame do pandas
    :param filename: Nome base do arquivo (ex: "users", "posts")
    :param output_dir: Diretório principal onde os arquivos serão armazenados
    """
    
    # Capturar data/hora atual no formato YYYYMMDD_HHhMMmSSs
    timestamp = datetime.now().strftime("%Y%m%d_%Hh%Mm%Ss")

    # Criar subpastas para CSV e JSON
    csv_dir = os.path.join(output_dir, "csv")
    json_dir = os.path.join(output_dir, "json")

    os.makedirs(csv_dir, exist_ok=True)
    os.makedirs(json_dir, exist_ok=True)

    # Gerar nomes dos arquivos com timestamp
    csv_path = os.path.join(csv_dir, f"{filename}_{timestamp}.csv")
    json_path = os.path.join(json_dir, f"{filename}_{timestamp}.json")

    # Salvar arquivos
    df.to_csv(csv_path, index=False)
    df.to_json(json_path, orient="records", indent=4)

    print(f"📂 Dados salvos em:\n- {csv_path}\n- {json_path}")

def normalize_and_display(data, name):
    """
    Normaliza um JSON para DataFrame, adiciona a coluna `dt_inc` e exibe os primeiros registros.

    :param data: JSON recebido da API
    :param name: Nome do DataFrame para exibição
    """
    
    df = pd.json_normalize(data)  # Normalizar JSON para DataFrame

    # Adicionar a coluna `dt_inc` com data/hora atual
    df['dt_inc'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n📊 DataFrame: {name}")
    print(df.head())  # Exibir as primeiras linhas do DataFrame

    return df