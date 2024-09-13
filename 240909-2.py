import os

try:
    os.system('cls')
    a = float(input('Informe um número: '))
    b = float(input('Informe outro número: '))
    resultado = a / b
except ZeroDivisionError:
    os.system('cls')
    print('\nDivisão por zero inválida!')
except ValueError:
    os.system('cls')
    print('\nFormato inválido!')
else:
    print(f'Resultado: {resultado}')
finally:
    print('\nEncerrando Programa...\n')