def busca(conjunto: list, valor: object) -> int:

    i = 0
    while i < len(conjunto) and conjunto[i] != valor:
        i += 1
    
    if i == len(conjunto):
        return -1
    else:
        return i

def elimina_repetidos(lista: list):

    resp= []
    
    for valor in lista:
        # Olhamos a lista resp para ver se o valor já está lá
        # Se não, ele é colocado em resp
        # Se sim, passamos para o próximo
        if busca(resp, valor) == -1:
            resp.append(valor)

    return resp

list = [2, 5, 6, 9, -1, 0, 7, 2, 4, 6, -1, 0]
resposta = elimina_repetidos(list)
print(resposta)
