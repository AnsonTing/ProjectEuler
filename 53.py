# Project Euler No. 53

import operator as op

def nCr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def solution():
    cnt = 0
    for n in range(1, 101):
        for r in range(1, n):
            if nCr(n, r) > 1000000:
                cnt += 1
    return cnt

print solution()
