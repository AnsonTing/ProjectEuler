# Project Euler No. 28

def spiral_diagonals_sum(num):
    max_num = num ** 2
    ans = 1
    n = 1
    step = 2
    while n <= max_num:
        n += step
        if n > max_num:
            break
        ans += n

        n += step
        if n > max_num:
            break
        ans += n

        n += step
        if n > max_num:
            break
        ans += n

        n += step
        if n > max_num:
            break
        ans += n

        step += 2

    return ans

print spiral_diagonals_sum(1001)
