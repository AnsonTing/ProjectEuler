# Project Euler No. 56

def sumOfDigits(n):
    return sum(int(d) for d in str(n))

def solution():
    maxSumOfDigits = 0
    for a in range(90, 101):
        for b in range(90, 101):
            maxSumOfDigits = max(maxSumOfDigits, sumOfDigits(a ** b))

    return maxSumOfDigits

print solution()
