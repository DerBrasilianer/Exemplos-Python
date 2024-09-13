import os

try:
    num = int(input('Informe um número inteiro: '))
    print(f'Você informou o número: {num}')
except ValueError:
    os.system('cls')
    print('Formato inválido!')