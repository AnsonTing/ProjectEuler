# Project Euler No. 44

def isPentagonal(num):
    n = ((24. * num + 1) ** 0.5 + 1) / 6.
    return int(n) == n


def solution():
    i = 2
    while True:
        m = i * (3 * i - 1) / 2
        for j in range(i-1, 0, -1):
            n = j * (3 * j - 1) / 2
            if isPentagonal(m + n) and isPentagonal(m - n):
                return m, n
        i += 1

print solution()
