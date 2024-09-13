def gravar_peca(matriz: list):

    #Vamos usar o separador ; (semicolon)
    #Vai criar um arquivo na mesma pasta com as peças inseridas

    arquivo = open('240902.csv', mode='w')

    for peca in matriz:
        
        for info in peca:

            arquivo.write(info)
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