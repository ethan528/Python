board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]

answer = 0


for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] != 0:
            answer += 1

print(answer)