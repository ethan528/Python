s = "try hello world"
ans = ''
for word in s.split(" "):
    for i, p in enumerate(word):
        print(i, p)
        if i % 2 == 0:
            ans += p.upper()
        else:
            ans += p.lower()
    ans += ' '
print(ans)