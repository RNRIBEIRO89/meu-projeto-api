import requests

def get_api_data(base_url, endpoint):
    """
    Faz uma requisição GET para um endpoint da API e retorna os dados em JSON.
    
    :param base_url: URL base da API
    :param endpoint: Endpoint específico da API (ex: 'users', 'posts')
    :return: Dados JSON ou erro
    """
    url = f"{base_url}/{endpoint}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"✅ Sucesso ao buscar {endpoint}")
        return response.json()  # Retorna os dados JSON
    else:
        print(f"❌ Erro ao buscar {endpoint} - Código {response.status_code}")
        return None