# Project Euler No. 40

def solution():
    s = ''
    n = 0
    while len(s) < 1000001:
        s += str(n)
        n += 1
    return int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) * int(s[10000]) * int(s[100000]) * int(s[1000000])

print solution()
