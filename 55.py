# Project Euler No. 55

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def solution():
    cnt = 0
    for num in range(1, 10001):
        n = int(num)
        for _ in range(50):
            n += int(str(n)[::-1])
            if isPalindrome(n):
                break
        else:
            print num
            cnt += 1

    return cnt

print solution()
