# Project Euler No. 43

from itertools import permutations as p

def solution():
    res = []
    permus = p('0123456789')
    for permu in permus:
        if permu[0] == '0':
            continue
        num = ''.join(permu)
        if int(num[1:4]) % 2 != 0: continue
        if int(num[2:5]) % 3 != 0: continue
        if int(num[3:6]) % 5 != 0: continue
        if int(num[4:7]) % 7 != 0: continue
        if int(num[5:8]) % 11 != 0: continue
        if int(num[6:9]) % 13 != 0: continue
        if int(num[7:10]) % 17 != 0: continue
        res.append(num)

    print res


solution()
