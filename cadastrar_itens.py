import os

class Item:
    grupo = None
    cod_item = None
    descricao = None
    local_estoque = None
    fabricante = None
    laudo = None

item1 = Item()

# Item p cadastrar
item1.grupo = 'Galpao'
item1.cod_item = 122
item1.descricao = 'Maquina de impressora 3d'
item1.local_estoque = 'central'
item1.fabricante = 'Fabricate B'
item1.laudo = 'Sim'

def ler_arquivo_csv():
    result = []
    
    # Ler arquivo e separar por linha
    file = open('base_cadastrar.csv','r').read().split('\n')

    # Faca para cada linha do arquivo
    for i,l in enumerate(file):
        if i == 0:
            continue

        if i >= (file.__len__() - 1):
            break

        item = Item()

        # Ler Linha do Arquivo e separar por coluna
        col = l.split(';')

        item.grupo = col[0]
        item.cod_item = col[1]
        item.descricao = col[2]
        item.local_estoque = col[3]
        item.fabricante = col[4]
        item.laudo = col[5]

        result.append(item)

    return result

def registro(des,cod_item):
    file_read = open('registro.txt','r').read()

    with open('registro.txt','w') as file:
        file.write(file_read)
        file.write( ' , '.join( [ des , cod_item , 'Cadastrado com sucesso !' ] ) + '\n' )
        file.close()