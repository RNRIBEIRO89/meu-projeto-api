# Importamos as configurações do projeto a partir do arquivo config.py
from config import BASE_API_URL, ENDPOINTS, OUTPUT_DIR

# Importamos a função que faz chamadas à API do arquivo api_client.py
from api_client import get_api_data

# Importamos as funções para processar e salvar os dados do arquivo data_processor.py
from data_processor import save_dataframe, normalize_and_display

def main():
    """
    Função principal que executa o processo de:
    1. Buscar dados da API.
    2. Converter os dados para um DataFrame.
    3. Exibir os dados.
    4. Salvar os dados em arquivos CSV e JSON.
    """
    
    # Percorre todos os endpoints definidos no arquivo config.py
    for endpoint in ENDPOINTS:
        print(f"\n🔍 Buscando dados do endpoint: {endpoint}")

        # Chama a função get_api_data() (definida em api_client.py) para buscar os dados da API
        data = get_api_data(BASE_API_URL, endpoint)

        # Verifica se a requisição foi bem-sucedida e se os dados foram retornados
        if data:
            print(f"✅ Dados obtidos do endpoint: {endpoint} ({len(data)} registros)")

            # Converte os dados JSON para um DataFrame e exibe as primeiras linhas
            df = normalize_and_display(data, name=f"Data - {endpoint}")

            # Salva o DataFrame em arquivos CSV e JSON dentro da pasta output/
            save_dataframe(df, filename=endpoint, output_dir=OUTPUT_DIR)

        else:
            # Caso a API falhe, exibe uma mensagem de erro
            print(f"❌ Erro ao obter dados do endpoint: {endpoint}")

# Este bloco garante que o código só será executado quando rodarmos este arquivo diretamente
if __name__ == "__main__":
    main()