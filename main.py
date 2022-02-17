import os
from os.path import isfile

def main():
    print('NC Leitor')
    relativePathFiles = input("Digite o caminho dos arquivos ou pressione [Enter] para continuar:")
    archivesList = handleReadArchives(relativePathFiles)
    handleProcessData(archivesList)

def handleReadArchives(relativePathFiles):
    # Verifica se foi passado o caminho
    if relativePathFiles is None or relativePathFiles == '' :
        relativePathFiles = "./archives"
    # Pega o caminho completo dos arquivos
    localFiles = os.path.abspath(relativePathFiles)
    # Carrega o arquivo na memoria
    os.chdir(localFiles)
    archivesNames = []
    #pega os nomes dos arquivos na pasta
    for archive in os.listdir():
        archivesNames.append(localFiles + '/' + archive)
    return archivesNames

def handleProcessData(archivesList):
    for archive in archivesList:
        with open(archive) as file:
            while fileLine := file.readline():
                print(fileLine.rstrip())


main()