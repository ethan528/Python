N = int(input())
GW = 0

for i in range(N):
    W = input()
    if len(set(W)) == len(W):
        GW += 1
    for j in W:
        temp = W[j+1:]
        F = temp.find(j)
        if   

print(GW)