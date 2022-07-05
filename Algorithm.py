N = int(input())
W = [input() for i in range(N)]
GW = 0

for i in range(N):
    if len(set(W[i])) == len(W[i]):
        GW += 1
    if len(W[i]) > 2:
        if W[i] 


print(GW)