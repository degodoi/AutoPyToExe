import subprocess
import ctypes

# Função para verificar se o usuário possui privilégios de administrador
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Função para executar o comando no cmd como administrador
def run_as_admin(command):
    if is_admin():
        subprocess.run(command, shell=True)
    else:
        # Se não for administrador, executa o comando como administrador
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/k {command}", None, 1)

# Comando a ser executado
comando = "auto-py-to-exe"

# Executar o comando como administrador
run_as_admin(comando)
