import subprocess
import sys

def instalar_pacote(pacote):
    try:
        __import__(pacote)  # Tenta importar o pacote
    except ImportError:
        # Se o pacote não estiver instalado, instala
        subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])

# Lista de pacotes necessários
pacotes_necessarios = ['deep-translator', 'tqdm']  # Exemplo de pacotes

def module():
    # Instala os pacotes necessários
    for pacote in pacotes_necessarios:
        instalar_pacote(pacote)