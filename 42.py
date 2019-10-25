# Project Euler No. 42

def solution():
    f = open('words.txt')
    words = eval(f.read())

    cnt = 0
    res = []
    for word in words:
        value = sum(ord(c) - 96 for c in word.lower())
        n = 1
        while n * (n + 1) / 2 < value:
            n += 1
        if n * (n + 1) / 2 == value:
            cnt += 1
            res.append(word)
    print res
    return cnt

print solution()
