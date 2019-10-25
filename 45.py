# Project Euler No. 45

def isPentagonal(num):
    return ((24. * num + 1) ** 0.5 + 1) % 6 == 0

def isTriangle(num):
    return ((8. * num + 1) ** 0.5 - 1) % 6 == 0

def isHexagonal(num):
    return ((8. * num + 1) ** 0.5 + 1) % 4 == 0

def solution():
    limit = 100000000
    n = 1
    while n < limit:
        Tri_num = n * (n + 1) / 2
        if isPentagonal(Tri_num) and isHexagonal(Tri_num):
            print n * (n + 1) / 2
        n += 1

solution()
