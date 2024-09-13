def busca(lista: list, valor, position):

    while position < len(lista) and lista[position] != valor:
        position = position + 1

    if position < len(lista):
        return position
    else:
        return -1
    
list = [2, 5, -7, 9, 3, 10, 15, 6]
x = 11

for i in range(len(list)):
    
    valor = x - list[i]
    resp = busca(list, valor, i + 1)

    if resp != -1:
        print (list[i], list[resp])