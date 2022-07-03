from string import ascii_uppercase

W = list(input())

n = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
a = list(ascii_uppercase)

p = {}
cnt = 0

for i in range(len(a)):    
    p[f"{a[i]}"] = n[i]

for i in W:
    if W != '':
        cnt += 2
    

print(p)