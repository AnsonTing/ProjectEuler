# Project Euler No. 50

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
    primes = []
    for n in range(2, len(l)):
        if l[n]:
            primes.append(n)
    return primes

def longestConsecutivePrimeSum(p, primes):
    maxCnt = 0
    for i in range(len(primes)):
        if primes[i] * 2 > p:
            return maxCnt
        cnt = 0
        j = int(i)
        primeSum = 0
        while primeSum < p:
            primeSum += primes[j]
            cnt += 1
            j += 1
        if primeSum == p:
            maxCnt = max(maxCnt, cnt)
    return maxCnt

def solution():
    primes = getPrimesBelowN(1000000)
    longestSeq = 0
    for p in reversed(primes):
        seq = longestConsecutivePrimeSum(p, primes)
        if seq > longestSeq:
            longestSeq = seq
            print p, seq

solution()
