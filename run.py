import os
import time
from main import main

def print_header():
    """
    Exibe um cabeçalho no terminal para indicar o início do processo.
    """
    print("\n" + "="*50)
    print("🚀 INICIANDO O PROCESSO DE COLETA E SALVAMENTO 🚀")
    print("="*50 + "\n")

def print_status(message):
    """
    Exibe uma mensagem indicando o andamento do processo.
    """
    print(f"➡️  {message}...")
    time.sleep(1)  # Adiciona um pequeno delay para melhor visualização

def print_success(message):
    """
    Exibe uma mensagem de sucesso.
    """
    print(f"✅ {message}\n")

def print_error(message):
    """
    Exibe uma mensagem de erro.
    """
    print(f"❌ {message}\n")

def check_directories():
    """
    Verifica se os diretórios de saída existem e os cria se necessário.
    """
    output_dirs = ["output", "output/csv", "output/json"]
    for directory in output_dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print_success(f"Pasta criada: {directory}")
        else:
            print_status(f"Pasta já existente: {directory}")

def execute_process():
    """
    Executa o processo principal e exibe mensagens indicando o progresso.
    """
    print_header()
    
    print_status("Verificando e criando diretórios")
    check_directories()

    print_status("Executando a extração de dados")
    try:
        main()  # Chama o processo principal do arquivo `main.py`
        print_success("Processo finalizado com sucesso!")
    except Exception as e:
        print_error(f"Erro durante a execução: {e}")

if __name__ == "__main__":
    execute_process()