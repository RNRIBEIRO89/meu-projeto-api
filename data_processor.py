import pandas as pd
import os
import logging
from datetime import datetime
from config import OUTPUT_DIR  # Importando o caminho correto

def save_dataframe(df, filename):
    """
    Salva um DataFrame em CSV e JSON no diretório correto `bucket_api/api_typicode/`.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%Hh%Mm%Ss")

    # Criar subpastas dentro do diretório de armazenamento correto
    csv_dir = os.path.join(OUTPUT_DIR, "csv")
    json_dir = os.path.join(OUTPUT_DIR, "json")

    os.makedirs(csv_dir, exist_ok=True)
    os.makedirs(json_dir, exist_ok=True)

    # Caminhos para salvar os arquivos
    csv_path = os.path.join(csv_dir, f"{filename}_{timestamp}.csv")
    json_path = os.path.join(json_dir, f"{filename}_{timestamp}.json")

    df.to_csv(csv_path, index=False)
    df.to_json(json_path, orient="records", indent=4)

    logging.info(f"📂 Dados salvos em: {csv_path}, {json_path}")

def normalize_and_display(data):
    """
    Normaliza um JSON para DataFrame e exibe os dados.
    """
    df = pd.json_normalize(data)
    df['dt_inc'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    logging.info(f"📊 Exibindo os primeiros 10 registros:\n{df.head(10)}")

    return df