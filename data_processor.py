import pandas as pd
import os
import logging
from datetime import datetime
from config import OUTPUT_DIR

def save_dataframe(df, filename):
    """
    Salva um DataFrame em CSV e JSON no diretório correto.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%Hh%Mm%Ss")
    csv_dir = os.path.join(OUTPUT_DIR, "csv")
    json_dir = os.path.join(OUTPUT_DIR, "json")

    os.makedirs(csv_dir, exist_ok=True)
    os.makedirs(json_dir, exist_ok=True)

    df.to_csv(os.path.join(csv_dir, f"{filename}_{timestamp}.csv"), index=False)
    df.to_json(os.path.join(json_dir, f"{filename}_{timestamp}.json"), orient="records", indent=4)

def normalize_and_display(data):
    """
    Normaliza um JSON para DataFrame.
    """
    df = pd.json_normalize(data)
    df['dt_inc'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return df