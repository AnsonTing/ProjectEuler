# Project Euler No. 30

l = []

for n in range(2, 10000000):
    if n == sum(int(d) ** 5 for d in str(n)):
        l.append(n)

print l
print sum(l)
