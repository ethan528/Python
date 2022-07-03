from string import ascii_uppercase

W = list(input())

n = [2,3,4,5,6,7,8,9]
a = list(ascii_uppercase)

p = {}
cnt = 0

if W:
    for i in a:
        if i == 7 or 9:
            temp = 4
        else:
            temp = 3
    for j in n:
        for _ in range(temp):
            p[f'{i}'] = j

print(p)