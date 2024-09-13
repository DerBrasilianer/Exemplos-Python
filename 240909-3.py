import os

def dividir(a, b):

    if b == 0:
        raise ZeroDivisionError('Divisão por zero inválida!')
    
    return a / b

try:
    os.system('cls')
    a = float(input('Informe um número: '))
    b = float(input('Informe outro número: '))
    resultado = dividir(a, b)
except ZeroDivisionError as e:
    os.system('cls')
    print(f'Erro: {e}')
except ValueError as f:
    os.system('cls')
    print(f'Erro: {f}')
else:
    print(f'Resultado: {resultado}')
finally:
    print('\nEncerrando Programa...\n')