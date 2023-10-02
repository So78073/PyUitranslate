import os
import subprocess


def uipy () :
    # Defina o caminho para o diretório (folder) que você deseja como diretório de trabalho atual
    caminho_para_diretorio = 'C:\\Users\\Shizu\\Desktop\\PROJETS\\PYTHON\\uipy'

    # Mude para o diretório de trabalho
    os.chdir(caminho_para_diretorio)

    # Substitua "seu_comando" pelo comando que você deseja executar no CMD no diretório especificado
    comando = 'pyuic6 -x main.ui -o test.py'

    # Execute o comando usando o subprocess
    try:
        resultado = subprocess.check_output(comando, shell=True, text=True)
        print("Saída do comando:")
        print(resultado)
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o comando:")
        print(e)