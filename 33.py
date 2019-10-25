# Project Euler No. 33

from fractions import Fraction as F

def solution():
    res = []
    for a in range(10, 100):
        for b in range(a+1, 100):
            if a % 10 == 0 and b % 10 == 0:
                continue
            la = [int(d) for d in str(a)]
            lb = [int(d) for d in str(b)]
            if la[0] == lb[0] and lb[1] and F(a, b) == F(la[1], lb[1]):
                res.append([(a, b), (la[1], lb[1])])
            if la[0] == lb[1] and lb[0] and F(a, b) == F(la[1], lb[0]):
                res.append([(a, b), (la[1], lb[0])])
            if la[1] == lb[0] and lb[1] and F(a, b) == F(la[0], lb[1]):
                res.append([(a, b), (la[0], lb[1])])
            if la[1] == lb[1] and lb[0] and F(a, b) == F(la[0], lb[0]):
                res.append([(a, b), (la[0], lb[0])])

    return res


print solution()
