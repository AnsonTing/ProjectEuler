# Project Euler No. 58

def getPrimesBelowN(n):
    l = [False, False] + [True] * (n-1)
    j = 4
    while j <= n:
        l[j] = False
        j += 2
    for i in range(3, n+1, 2):
        if l[i]:
            j = i * 2
            while j <= n:
                l[j] = False
                j += i
    return l

def isPrime(n):
    if n % 2 == 0:
        return False
    for i in xrange(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def solution():
    limit = 700000000
    n = 1
    primesCnt = 0
    numbersCnt = 1
    step = 2
    while n + 4 * step < limit:
        for _ in range(3):
            n += step
            if isPrime(n):
                primesCnt += 1
        n += step
        numbersCnt += 4
        print str(primesCnt * 100. / numbersCnt) + '%'
        if primesCnt * 10 < numbersCnt:
            return step + 1
        step += 2

print solution()
