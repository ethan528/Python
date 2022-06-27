a, b, c = map(int, input().split())
p = 0

if a == b == c:
    p = 10000 + (a*1000)
elif a == b:
    p = 1000 + (a*100)
elif a == c:
    p = 1000 + (a*100)
elif b == c:
    p = 1000 + (a*100)
else:
    p = max(a,b,c)*100

print(p)