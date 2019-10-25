# Project Euler No. 38

def solution():
    n = 1
    limit = 100000
    while n < limit:
        s = list(str(n))
        for m in range(2, 10):
            s += str(n * m)
            if len(s) > 9:
                break
            if sorted(s) == list('123456789'):
                print n, s
                break
        n += 1

solution()
