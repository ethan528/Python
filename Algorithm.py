N = int(input())
GW = 0

for i in range(N):
    W = input()
    TS = 0
    if len(set(W)) == len(W):
        GW += 1
        print('1',W)
    for j in range(len(W)):
        print(j)
        K = W[j+1:]
        print('k',K)
        F = K.find(W[j])
        print('f',F)
        R = int(W.find(W[j])) + int(F)
        print('r',R, j-1)
        if R == (j-1) or R == j or len(K) == 1:
            TS += 1
            print(W[j], 'TS', TS, len(W))
        elif K == '':
            pass
        else:
            pass
    if len(W) == TS:
        GW += 1
        print('2',W, 'GW', GW)

print(GW)