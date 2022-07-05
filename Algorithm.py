N = int(input())
W = [input() for i in range(N)]
GW = 0

for i in range(N):
    TS = 0
    for j in range(len(W[i])):
        if W[i][j] not in W[i][j+2:] or W[i][j] not in W[i][j-2:]:
            TS += 1
        if len(set(W[i])) == len(W[i]):
            TS += len(W[i])
        if len(set(W[i])) == 1:
            TS += 1
            if TS == len(W[i]):
                GW += 1

print(GW)