word = list(input())
cnt = 0

for i in word:
    temp = word.count(i)
    print(type(temp))
    print(type(cnt))
    if temp > cnt:
        cnt = temp
        answer = i
    elif temp == cnt:
        answer = '?'

print(cnt.upper())