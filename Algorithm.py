N = int(input())
M = 1
F = 1

while N:
    if N == 1:
        print(F)
    else:
        M += 5 * M + F
        F += 1
        if  N <= M:
            print(F)
            break