import requests
import logging

def get_api_data(base_url, endpoint):
    """
    Faz uma requisição GET para um endpoint da API e retorna os dados em JSON.
    """
    url = f"{base_url}/{endpoint}"
    response = requests.get(url)

    if response.status_code == 200:
        logging.info(f"✅ Sucesso ao buscar {endpoint}")
        return response.json()
    else:
        logging.error(f"❌ Erro ao buscar {endpoint} - Código {response.status_code}")
        return None