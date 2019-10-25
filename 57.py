# Project Euler No. 57

from fractions import Fraction as F

def solution():
    f = F(1, 2)
    iteration_no = 1
    cnt = 0
    while iteration_no < 1000:
        n = f.numerator
        d = f.denominator
        if len(str(n+d)) > len(str(d)):
            cnt += 1
        f = 1 / (2 + f)
        iteration_no += 1
    return cnt

print solution()
