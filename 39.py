# Project Euler No. 39

def solution():
    max_sol = 0
    max_sol_p = None
    for p in range(3, 1001):
        sol = 0
        for a in range(1, p // 3 + 1):
            for b in range(a, p):
                c = p - a - b
                if b > c:
                    break
                if a ** 2 + b ** 2 == c ** 2:
                    sol += 1
        if sol > max_sol:
            max_sol = sol
            max_sol_p = p
    print max_sol, max_sol_p

solution()
