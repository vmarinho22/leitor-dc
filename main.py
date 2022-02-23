import os
from os.path import isfile
from datetime import datetime

def main():
    print('NC Leitor')
    relativePathFiles = input("Digite o caminho dos arquivos ou pressione [Enter] para continuar:")
    archivesCount = handleGetNumberFiles(relativePathFiles)
    archivesList = handleReadArchives(relativePathFiles)
    newFile = handleProcessData(archivesList, archivesCount)
    handleCreateFinalFile(newFile)

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

def handleProcessData(archivesList, archivesCount):
    # Varre o array de arquivos
    count = 1
    newFile = []
    rule = globalRules(archivesCount);
    for archive in archivesList:
        # Abre o arquivo na memoria e varre linha a linha
        num_lines = sum(1 for line in open(archive))
        with open(archive) as file:
            while fileLine := file.readline():
                line = fileLine.rstrip()
                newFile.append(handleApplyLineRule(line, rule[count]['sum']))
        ruleRemove = rule[count]['remove']
        if(rule[count]['remove'] == 2):
            newFile = newFile[:-1]
            newFile = newFile[:-1]
        newFile.append(rule[count]['add'])
        count = count + 1
    print('Dados processados com sucesso!');
    return newFile

def handleApplyLineRule(line, rule):
    lineArray = line.split(' ');
    finalLine = ''
    for chunk in lineArray:
        if(chunk[0] == 'X'):
            lineNumber = chunk[1:]
            floatNumber = float(lineNumber) + rule
            finalLine += 'X' + str(floatNumber) + ' '
        else:
            finalLine += chunk + ' '
    return finalLine;

def globalRules(number):
    switcher = {
        2: {
            1: {
                'sum': 0,
                'remove': 2,
                'add': 'G01 X40 \n G00 Y1 \n X80'
            },
            2: {
                'sum': 80,
                'remove': 2,
                'add': ''
            },
        },
        3: {
            1: {
                'sum': 0,
                'remove': 2,
                'add': 'G01 X40 \n G00 Y1 \n X80'
            },
            2: {
                'sum': 80,
                'remove': 2,
                'add': 'G01 X120 \n G00 Y1 \n X160'
            },
            3: {
                'sum': 160,
                'remove': 2,
                'add': ''
            },
        },
        4: {
            1: {
                'sum': 0,
                'remove': 2,
                'add': 'G01 X40 \n G00 Y1 \n X80'
            },
            2: {
                'sum': 160,
                'remove': 2,
                'add': 'G01 X120 \n G00 Y1 \n X160'
            },
            3: {
                'sum': 160,
                'remove': 2,
                'add': 'G01 X200 \n G00 Y1 \n X240'
            },
            4: {
                'sum': 240,
                'remove': 0,
                'add': ''
            },
        },
    }
    return switcher.get(number,"Invalid rule number")


def handleGetNumberFiles(relativePathFiles):
    # Verifica se foi passado o caminho
    if relativePathFiles is None or relativePathFiles == '' :
        relativePathFiles = "./archives"
    # Pega o caminho completo dos arquivos
    localFiles = os.path.abspath(relativePathFiles)
    #Le os arquivos da mémoria
    list = os.listdir(localFiles) 
    # Conta quantos arquivos existem
    number_files = len(list)
    return(number_files)

def handleCreateFinalFile(array):
    if not os.path.exists('../reports'):
        os.makedirs('../reports')
    localFiles = os.path.abspath('../reports')
    # Carrega o arquivo na memoria
    os.chdir(localFiles)
    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    with open("Report_"+ date +".nc", "w") as txt_file:
        for line in array:
            txt_file.write("".join(line) + "\n")
    print('Arquivo gerado com sucesso na pasta reports: '+ "Report_"+ date +".nc")

main()