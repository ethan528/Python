n = 3
m= 12
def solution(n, m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]

print(solution(n, m))

if not 3%3:
    print(3%3)