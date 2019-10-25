# Project Euler No. 49

from itertools import permutations as p

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

def solution():
    l = getPrimesBelowN(10000)
    for a in range(1000, len(l)):
        if l[a]:
            permus = [int(''.join(permu)) for permu in p(str(a))]
            for b in permus:
                if not l[b]:
                    continue
                if a >= b:
                    continue
                c = 2 * b - a
                if c not in permus:
                    continue
                if not l[c]:
                    continue
                print a, b, c

solution()
