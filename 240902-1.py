import os
os.system('cls')

def inserir_peca(matriz: list):
    os.system('cls')

    nome = input('Nome: ')
    serie = input('Nº de Série: ')
    origem = input('Origem: ')
    preco = float(input('Preço: '))
    quantidade = int(input('Quantidade: '))

    registro = [nome, serie, origem, preco, quantidade]
    matriz.append(registro)

def alterar_peca(matriz: list):
    os.system('cls')

    serie = input('Nº de Série: ')
    pos = busca(matriz, serie)

    if pos == -1:
        print('Não existe.')
    else:

        registro = matriz[pos]

        nome = input(f'Nome ({registro[0]}): ')
        if len(nome) > 0:
            registro[0] = nome
        
        serie = input(f'Nº de Série: ({registro[1]}): ')
        if len(serie) > 0:
            registro[1] = serie
        
        origem = input(f'Origem: ({registro[2]}): ')
        if len(origem) > 0:
            registro[2] = origem

        preco = input(f'Preço: ({registro[3]}): ')
        if len(preco) > 0:
            registro[3] = float(preco)
        
        quantidade = input(f'Origem: ({registro[4]}): ')
        if len(quantidade) > 0:
            registro[4] = quantidade

def consultar_peca(matriz: list):
    os.system('cls')

    origem = input('Informe a origem: ')

    for i in range(len(matriz)):

        if matriz[i][2] == origem:

            print(matriz[i])

def busca(matriz: list, serie: str):

    for i in range(len(matriz)):

        if matriz[i][1] == serie:

            return i
        
    return -1

def excluir_peca(matriz: list):
    os.system('cls')

    serie = input('Informe o Nº de Série: ')

    pos = busca(matriz, serie)

    if pos == -1:
        print('Nenhuma peça encontrada!')
    else:
        info = matriz.pop(pos)
        print(info)
        print('Excluído com sucesso!')

def gravar_peca(matriz: list):

    #Vamos usar o separador ; (semicolon)
    #Vai criar um arquivo na mesma pasta com as peças inseridas

    arquivo = open('240902.csv', mode='w')

    for peca in matriz:
        
        for info in peca:

            arquivo.write(str(info))
            arquivo.write(';')

        arquivo.write('\n')

    arquivo.close()

    print('Arquivo gravado com sucesso!')

def ler_pecas(nome: str) -> list:

    arquivo = open(nome, mode='r')
    resultado = []

    for linha in arquivo:
        campos = linha.split(';')
        registro = [campos[0], campos[1], campos[2], float(campos[3]), int(campos[4])]
        resultado.append(registro)
    
    return resultado

def encerrar():
    os.system('cls')
    print('Encerrando Programa!')
    return

if __name__ == '__main__':

    opcao = 0
    estoque = ler_pecas('240902.csv')

    while (opcao != 6):

        print('------------------')
        print('SISTEMA DE PEÇAS')
        print('------------------')
        print('1. Inserir')
        print('2. Alterar')
        print('3. Consultar')
        print('4. Excluir')
        print('5. Gravar')
        print('6. Sair')

        opcao = int(input('Selecione uma opção: '))

        if opcao == 1:
            inserir_peca(estoque)
        elif opcao == 2:
            alterar_peca(estoque)
        elif opcao == 3:
            consultar_peca(estoque)
        elif opcao == 4:
            excluir_peca(estoque)
        elif opcao == 5:
            gravar_peca(estoque)
        elif opcao == 6:
            encerrar()

