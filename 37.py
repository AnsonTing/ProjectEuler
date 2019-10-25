# Project Euler No. 37

def getPrimesBelowN(n):
    l = [False, False] + [True] * (n-1)
    j = 4
    while j <= n:
        l[j] = False
        j += 2
    for i in range(3, n+1, 2):
        if l[i]:
            j = i * 2
            while j <= n:
                l[j] = False
                j += i
    return l

def solution():
    # There are only 11 truncatable primes (excluding 2, 3, 5, 7)
    truncatable_primes = []
    limit = 1000000
    l = getPrimesBelowN(limit)
    for n in range(11, len(l)):
        if l[n]:
            # n is prime
            truncatable = True
            # truncate left
            p = str(n)
            while len(p) > 1:
                p = p[1:]
                if not l[int(p)]:
                    truncatable = False
                    break
            if truncatable:
                # truncate right
                p = str(n)
                while len(p) > 1:
                    p = p[:-1]
                    if not l[int(p)]:
                        truncatable = False
                        break
            if truncatable:
                truncatable_primes.append(n)
    return truncatable_primes

print sum(solution())
