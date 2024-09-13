import time

def busca(conjunto: list, valor: object) -> int:

    i = 0
    while i < len(conjunto) and conjunto[i] != valor:
        i += 1
    
    if i == len(conjunto):
        return -1
    else:
        return i

def busca_for(conjunto: list, valor: object) -> int:

    for i in range(len(conjunto)):
        if conjunto[i] == valor:
            return i 
        
    return -1

lst = [0] * 1_000
x = 1
ini = time.time()
resp = busca(lst, x)
fim = time.time()
print(fim - ini, "Busca com while")

ini = time.time()
resp = busca_for(lst, x)
fim = time.time()
print(fim - ini, "Busca com for")