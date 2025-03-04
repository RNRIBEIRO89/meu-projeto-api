from config import BASE_API_URL, ENDPOINTS
from api_client import get_api_data
from data_processor import save_dataframe, normalize_and_display
import logging

def main():
    """
    Executa o processo ETL de Extração, Transformação e Carregamento.
    """
    logging.info("🚀 Iniciando processo ETL")
    logging.info(f"🔗 API Base: {BASE_API_URL}")

    for endpoint in ENDPOINTS:
        logging.info(f"📌 Processando Endpoint: {endpoint.upper()}")

        # Extração dos dados
        data = get_api_data(BASE_API_URL, endpoint)
        if not data:
            logging.error(f"❌ Erro ao obter dados do endpoint `{endpoint}`")
            continue

        # Transformação dos dados
        df = normalize_and_display(data)
        row_count, col_count = df.shape
        logging.info(f"📊 Estrutura do DataFrame `{endpoint}`: {row_count} linhas, {col_count} colunas")

        # Carregamento dos dados
        save_dataframe(df, filename=endpoint)
        logging.info(f"✅ Dados `{endpoint}` salvos com sucesso")

    logging.info("✅ Processo ETL concluído!")

if __name__ == "__main__":
    main()