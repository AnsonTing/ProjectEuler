# Project Euler No. 34

from math import factorial

def solution():
    res = []
    for n in range(10, 100000):
        if n == sum(factorial(int(d)) for d in str(n)):
            res.append(n)

    return sum(res)

print solution()
