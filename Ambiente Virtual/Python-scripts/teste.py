import subprocess

def main():

    virtual_env_path = 'C:/Users/camis/OneDrive/Documentos/PROJETOS VERSIONADOS/playing-with-UiPath/Ambiente Virtual/Python-scripts'

    subprocess.run(['poetry', 'install'], cwd = virtual_env_path, shell=True)

    #subprocess.run(['poetry', 'shell'], cwd = virtual_env_path, shell=True)

    script_name = 'scriptExample.py'

    subprocess.run(['poetry','run', 'python', script_name], cwd= virtual_env_path, shell=True)
