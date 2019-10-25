# Project Euler No. 46

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

def isPerfectSquare(n):
    return n == int(n ** 0.5) ** 2

def solution():
    limit = 10000
    l = getPrimesBelowN(limit)
    for n in range(3, limit, 2): # Odd number
        if not l[n]: # Composite number
            for m in range(2, n):
                if l[m] and isPerfectSquare((n - m) / 2.):
                    print '%d=%d+2*(%d**2)' % (n, m, int(((n - m) / 2.) ** 0.5))
                    break
            else:
                return n

print solution()
