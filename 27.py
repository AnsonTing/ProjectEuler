# Project Euler No. 27

def isPrime(n):
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i==0:
            return False
    return True

def no_of_primes_produced_by_formula(a, b):
    for n in range(1001):
        if not isPrime(n ** 2 + a * n + b):
            return n


max_no_of_primes_produced = -1

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        res = no_of_primes_produced_by_formula(a, b)
        if res > max_no_of_primes_produced:
            max_no_of_primes_produced = res
            print a, b, res
