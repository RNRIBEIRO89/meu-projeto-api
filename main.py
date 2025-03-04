from config import BASE_API_URL, ENDPOINTS
from api_client import get_api_data
from data_processor import save_dataframe, normalize_and_display
import logging
import pandas as pd
import json

def log_and_print(message, level="info"):
    """
    Exibe uma mensagem no terminal e registra no arquivo de log.
    """
    print(message)
    if level == "info":
        logging.info(message)
    elif level == "error":
        logging.error(message)

def main():
    """
    Executa o processo ETL de Extração, Transformação e Carregamento.
    """
    log_and_print("🚀 Iniciando processo ETL...\n")
    log_and_print(f"🔗 API Base: {BASE_API_URL}")

    for endpoint in ENDPOINTS:
        log_and_print("\n" + "="*60)
        log_and_print(f"📌 Endpoint: {endpoint.upper()}")
        log_and_print("="*60)

        # Extração dos dados
        log_and_print(f"➡️  Buscando dados do endpoint `{endpoint}`...")
        data = get_api_data(BASE_API_URL, endpoint)

        if not data:
            log_and_print(f"❌ Falha ao obter dados do endpoint `{endpoint}`", level="error")
            continue

        log_and_print(f"✅ Dados brutos recebidos de `{endpoint}`:")
        log_and_print(json.dumps(data[:3], indent=4))  # Exibe os 3 primeiros registros para validar

        # Transformação dos dados
        log_and_print("🔄 Normalizando JSON com `pd.json_normalize()`...")
        df = normalize_and_display(data)

        log_and_print(f"📊 Dataset `{endpoint}`: {df.shape[0]} linhas, {df.shape[1]} colunas")

        # Exibir as 5 primeiras linhas para validar
        log_and_print("🔍 Exemplo dos primeiros registros do DataFrame:")
        log_and_print(df.head(5).to_string())

        # Carregamento dos dados (Salvar CSV e JSON)
        log_and_print("💾 Convertendo para CSV e JSON...")
        save_dataframe(df, filename=endpoint)

        log_and_print(f"✅ Dados de `{endpoint}` salvos com sucesso!")

    log_and_print("\n✅ Processo ETL concluído!")

if __name__ == "__main__":
    main()