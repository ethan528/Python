a, b = map(int, input().split())
c = int(input())


if b+c >= 60 and a == 23:
    a = 0
    b = b+c-60
if b+c >= 60:
    a = a+1
    b = b+c-60
while b >= 60:
    a = a+1
    b = b-60

print(a,b)