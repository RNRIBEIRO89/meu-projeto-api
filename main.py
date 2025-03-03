from config import BASE_API_URL, ENDPOINTS, OUTPUT_DIR
from api_client import get_api_data
from data_processor import save_dataframe, normalize_and_display
import logging

def main():
    """
    Executa o processo ETL de Extração, Transformação e Carregamento.
    """
    logging.info("🚀 Iniciando processo ETL...")

    for endpoint in ENDPOINTS:
        logging.info(f"🔍 Processando endpoint: {endpoint.upper()}")

        # Extração dos dados
        data = get_api_data(BASE_API_URL, endpoint)
        if not data:
            logging.error(f"❌ Falha ao obter dados do endpoint {endpoint}")
            continue

        # Transformação dos dados
        df = normalize_and_display(data)
        logging.info(f"✅ {endpoint}: {len(df)} registros extraídos")

        # Carregamento dos dados (Salvar CSV e JSON no diretório correto)
        save_dataframe(df, filename=endpoint)

    logging.info("✅ Processo ETL concluído!")

if __name__ == "__main__":
    main()