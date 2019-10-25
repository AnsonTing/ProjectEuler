# Project Euler No. 32

def solution():
    res = []
    ans_set = set()
    for a in range(1, 100):
        for b in range(1, 10000):
            c = a * b
            if sorted(''.join(str(n) for n in [a, b, c])) == list('123456789'):
                res.append([a, b, c])
                ans_set.add(c)

    for r in res:
        print str(r[0]) + '*' + str(r[1]) + '=' + str(r[2])

    print ans_set
    print sum(ans_set)

solution()
