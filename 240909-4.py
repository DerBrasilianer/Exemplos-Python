import os

digitou_certo = False

os.system('cls')
while not digitou_certo:

    try:
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        salario = float(input('Salário: '))
        digitou_certo = True
    except:
        print('\nErro no informe, digite novamente!\n')

print(f'\nNome: {nome}, \nIdade: {idade}, \nSalário: {salario}')