import random
import os

matriz = []

for _ in range(5):
    matriz.append([0] * 7)

for i in range(5):
    for j in range(7):
        matriz[i][j] = random.randint(0, 1000)

os.system('cls')
for linha in matriz:
    print(linha)