import os
os.system('cls')

def busca(valor: object, matriz: list) -> list:

    linha = len(matriz)
    coluna = len(matriz[0])

    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] == valor:
                return (f'Posição: {[i, j]}')
            
    return (f'{[-1, -1]}, Elemento não encontrado!')

mat = [
    [9, 92, 8, 5],
    [-1, 5, 7, 10],
    [4, 7, 9, 15]
]

resposta = busca(int(input('Que número deseja buscar na matriz? ')), mat)
print(resposta)