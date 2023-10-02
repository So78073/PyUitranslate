import os
import subprocess


def uipy () :

    caminho_para_diretorio = 'C:\\Users\\Shizu\\Desktop\\PROJETS\\PYTHON\\uipy'

  
    os.chdir(caminho_para_diretorio)


    comando = 'pyuic6 -x main.ui -o test.py'


    try:
        resultado = subprocess.check_output(comando, shell=True, text=True)
        print("Saída do comando:")
        print(resultado)
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o comando:")
        print(e)