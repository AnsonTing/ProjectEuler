# Project Euler No. 47

def getPrimeFactors(n):
    if n == 1: return []
    factors = []
    cnt = 0
    while n % 2 == 0:
        n /= 2
        cnt += 1
    if cnt:
        factors.append((2, int(cnt)))
    f = 3
    while n > 1:
        if f ** 2 > n:
            factors.append((n, 1))
            break
        cnt = 0
        while n % f == 0:
            n /= f
            cnt += 1
        if cnt:
            factors.append((f, int(cnt)))
        f += 2
    return factors


def solution():
    n = 2
    a = getPrimeFactors(n)
    b = getPrimeFactors(n+1)
    c = getPrimeFactors(n+2)
    d = getPrimeFactors(n+3)
    while True:
        if len(a) == len(b) == len(c) == len(d) == 4:
            print a, b, c, d
            return n
        a, b, c, d = b, c, d, getPrimeFactors(n+4)
        n += 1

print solution()
