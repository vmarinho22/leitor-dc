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
    # Varre o array de arquivos
    archiveCount = 0
    for archive in archivesList:
        # Abre o arquivo na memoria e varre linha a linha
        with open(archive) as file:
            count = 0
            while fileLine := file.readline():
                line = fileLine.rstrip()
        archiveCount++


main()