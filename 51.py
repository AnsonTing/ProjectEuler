# Project Euler No. 51

from itertools import combinations as c

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
    l = getPrimesBelowN(1000000)
    for n in range(len(l)):
        if l[n]:
            digits = len(str(n))
            for length in range(1, digits):
                combs = c(range(digits), length)
                for comb in combs:
                    replacement_prime = []
                    d_replacement = '123456789'
                    if 0 not in comb:
                        d_replacement = '0123456789'
                    for d in d_replacement:
                        p = list(str(n))
                        for pos in comb:
                            p[pos] = d
                        if l[int(''.join(p))] and int(''.join(p)) not in replacement_prime:
                            replacement_prime.append(int(''.join(p)))
                            if len(replacement_prime) >= 8:
                                print sorted(replacement_prime)




solution()
