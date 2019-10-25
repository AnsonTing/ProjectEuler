# Project Euler No. 35

from itertools import combinations_with_replacement as c
from itertools import permutations as p

def solution():
    limit = 1000000
    l = getPrimesBelowN(limit)

    res_set = set()
    for i in range(2, len(l)):
        if l[i]:
            rotations = []
            p = i
            while p not in rotations:
                rotations.append(p)
                p = int(str(p)[-1] + str(p)[:-1])
            if all(l[p] for p in rotations):
                for p in rotations:
                    res_set.add(p)
    return len(res_set)



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




print solution()
