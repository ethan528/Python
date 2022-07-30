a, b, v = map(int, input().split())
h = 0
d = 0

while v:
    if d%2 == 0:
        h += a
    if d%2 != 0:
        h -= b
        if h <= v:
            d += 1
    if h >= v:
        break

print(d)
