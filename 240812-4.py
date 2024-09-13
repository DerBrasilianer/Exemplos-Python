def encontrar_menor(lista: list, pos: int):

    ind = pos

    while pos< len(lista):
        if lista[pos] < lista[ind]:
            ind = pos
        pos += 1
    return ind

def selection_sort(lista: list):
    i = 0

    while i < len(lista):
        pos = encontrar_menor(lista, i)
        aux = lista[pos]
        lista[pos] = lista[i]
        lista[i] = aux
        i += 1

lista = [3, 4, 9, 0, 8]
selection_sort(lista)
print(lista)