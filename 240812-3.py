def esta_ordenada(conjunto: list) -> bool:

    i = 0
    while i < len(conjunto) -1:
        
        if conjunto[i] > conjunto[i + 1]:
            return False
        i += 1

    return True
        
        
lista = [1, 1, 2, 3, 2]
r = esta_ordenada(lista)
print(r)