import os
import logging
from main import main

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

log_filename = os.path.join(LOG_DIR, "execution.log")
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def execute_process():
    """
    Executa o processo principal e exibe logs.
    """
    print("🚀 Iniciando execução...")
    main()
    print("✅ Execução concluída!")

if __name__ == "__main__":
    execute_process()