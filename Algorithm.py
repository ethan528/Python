N = int(input())
W = [input() for i in range(N)]
GW = 0

for i in range(N):
    TS = 0
    for j in range(len(W[i])):
        try:
            if W[i][j] != W[i][j+1] and W[i][j] == W[i][j+2]:
                TS += 1
        except IndexError:
            TS += 1
        if len(set(W[i])) == len(W[i]):
            TS += 1
            if len(W[i]) == TS:
                GW += 1

print(GW)