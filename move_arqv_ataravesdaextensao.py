import os
import shutil


origem= "caminho:\\de origem \\de onde esta seu trabalho"

#criando pasta para armazenar arquivos
os.mkdir("D:\\criando pasta\\nome da pasta")
caminho= "D:\\criando pasta\\nome da pasta"
#selecionando arquivos atraves da sua extensao
arquivo_C=[arquivo for arquivo in os.listdir(origem) if arquivo.endswith(".c")]
for arquivo in arquivo_C:
    print(arquivo)
    caminho_completo= os.path.join(origem,arquivo)
    caminho_destino= os.path.join(caminho,arquivo)
    shutil.move(caminho_completo,caminho_destino)



