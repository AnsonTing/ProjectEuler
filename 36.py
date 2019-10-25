# Project Euler No. 36

def solution():
    limit = 1000000
    res_set = []
    for n in range(1, limit+1):
        if isPalindrome(n) and isPalindrome(bin(n)[2:]):
            res_set.append(n)
    return sum(res_set)


def isPalindrome(n):
    # type of n: int or string
    return str(n) == str(n)[::-1]

print solution()
