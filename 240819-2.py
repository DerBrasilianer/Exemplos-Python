def imprime(matriz):
    for linha in matriz:
        print(linha)

board = []
i = 0
while i < 3:
    board.append(['']*3)
    i += 1

imprime(board)

board[0][0] = 'X'
board[1][1] = 'O'
board[2][2] = 'X'

imprime(board)