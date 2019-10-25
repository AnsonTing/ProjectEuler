# Project Euler No. 48

def solution():
    ans = 0
    for n in range(1, 1001):
        ans += n ** n
        ans %= 10000000000
    return ans

print solution()
