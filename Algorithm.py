n = 10

answer = []
print(int(n**(1/2)))
for i in range(1, int(n**(1/2)) + 1):
    print('i', i)
    if n % i == 0:
        answer.append(i) 
        print('i', i)
        if i**2 != n : 
            answer.append(n // i)
            print('n//i', n//i)
            
print(sum(answer))